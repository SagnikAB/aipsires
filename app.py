from flask import Flask, render_template, request, redirect, url_for, flash
import os
import uuid
from werkzeug.utils import secure_filename

from core.resume_parser import extract_text
from core.scoring_engine import score_resume
from core.database import init_db, save_resume, get_all_resumes


# ===============================
# APP CONFIGURATION
# ===============================
app = Flask(__name__, template_folder="templates", static_folder="static")

app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key")

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf", "doc", "docx"}
MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5MB

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = MAX_CONTENT_LENGTH

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

init_db()


# ===============================
# HELPER FUNCTIONS
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
        flash("Invalid file type.")
        return redirect(url_for("home"))

    try:
        original_name = secure_filename(file.filename)
        unique_name = f"{uuid.uuid4().hex}_{original_name}"
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], unique_name)
        file.save(filepath)

        text = extract_text(filepath)

        if not text.strip():
            flash("Could not extract text.")
            return redirect(url_for("home"))

        score, keywords = score_resume(text)

        save_resume(original_name, score, keywords)

        rank = get_rank(score)

        return render_template(
            "result.html",
            score=score,
            keywords=keywords,
            rank=rank
        )

    except Exception as e:
        print(e)
        flash("Error analyzing resume.")
        return redirect(url_for("home"))


@app.route("/history")
def history():
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


# ===============================
# ERROR HANDLERS
# ===============================
@app.errorhandler(413)
def file_too_large(e):
    flash("File too large.")
    return redirect(url_for("home"))


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404 Page Not Found</h1>", 404


# ===============================
# RUN
# ===============================
if __name__ == "__main__":
    app.run(debug=True)