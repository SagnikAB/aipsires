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
MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5MB limit

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = MAX_CONTENT_LENGTH


# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize database
init_db()


# ===============================
# HELPER FUNCTIONS
# ===============================
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


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
        flash("Invalid file type. Only PDF, DOC, DOCX allowed.")
        return redirect(url_for("home"))

    try:
        # Secure + Unique filename
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

        # Save to database
        save_resume(original_name, score, keywords)

        return render_template(
            "result.html",
            score=score,
            keywords=keywords
        )

    except Exception as e:
        print("Error:", e)
        flash("Something went wrong while analyzing the resume.")
        return redirect(url_for("home"))


@app.route("/history")
def history():
    try:
        data = get_all_resumes()
        return render_template("history.html", data=data)
    except Exception as e:
        print("Database error:", e)
        flash("Unable to fetch history.")
        return redirect(url_for("home"))


# ===============================
# ERROR HANDLERS
# ===============================

@app.errorhandler(413)
def file_too_large(e):
    flash("File too large. Maximum size is 5MB.")
    return redirect(url_for("home"))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


# ===============================
# RUN SERVER
# ===============================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug_mode = os.environ.get("FLASK_ENV") == "development"

    app.run(host="0.0.0.0", port=port, debug=debug_mode)
