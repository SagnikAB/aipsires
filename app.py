from flask import Flask, render_template, request, redirect, url_for, flash
import os
import uuid
from werkzeug.utils import secure_filename

from core.resume_parser import extract_text
from core.scoring_engine import score_resume
from core.database import init_db, save_resume, get_all_resumes


# ===============================
# APP CONFIG
# ===============================
app = Flask(__name__, template_folder="templates", static_folder="static")

app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key")

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf", "doc", "docx"}
MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5MB

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = MAX_CONTENT_LENGTH

# Create upload folder if not exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize DB
init_db()


# ===============================
# HELPERS
# ===============================
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def get_rank(score):
    if score >= 90:
        return "🏆 Elite"
    elif score >= 75:
        return "🥇 Gold"
    elif score >= 60:
        return "🥈 Silver"
    else:
        return "🥉 Bronze"


# ===============================
# ROUTES
# ===============================

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    if "resume" not in request.files:
        flash("No file uploaded.")
        return redirect(url_for("home"))

    file = request.files["resume"]

    if file.filename == "":
        flash("Please select a file.")
        return redirect(url_for("home"))

    if not allowed_file(file.filename):
        flash("Invalid file type. Only PDF/DOC/DOCX allowed.")
        return redirect(url_for("home"))

    try:
        # Save file
        original_name = secure_filename(file.filename)
        unique_name = f"{uuid.uuid4().hex}_{original_name}"
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], unique_name)
        file.save(filepath)

        # Extract text
        text = extract_text(filepath)

        if not text.strip():
            flash("Could not extract text from resume.")
            return redirect(url_for("home"))

        # Score resume
        score, keywords = score_resume(text)

        # Save to DB
        save_resume(original_name, score, keywords)

        # Rank
        rank = get_rank(score)

        return render_template(
            "result.html",
            score=score,
            keywords=keywords,
            rank=rank
        )

    except Exception as e:
        print("ERROR:", e)
        flash("Something went wrong.")
        return redirect(url_for("home"))


@app.route("/history")
def history():
    try:
        data = get_all_resumes()

        enhanced = []
        for item in data:
            filename, score, keywords = item
            enhanced.append({
                "filename": filename,
                "score": score,
                "keywords": keywords,
                "rank": get_rank(score)
            })

        return render_template("history.html", data=enhanced)

    except Exception as e:
        print("DB ERROR:", e)
        flash("Could not load history.")
        return redirect(url_for("home"))


# ===============================
# ERROR HANDLERS
# ===============================
@app.errorhandler(413)
def too_large(e):
    flash("File too large (Max 5MB)")
    return redirect(url_for("home"))


@app.errorhandler(404)
def not_found(e):
    return "<h1>404 Page Not Found</h1>", 404


# ===============================
# RUN SERVER (RENDER FIX)
# ===============================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)