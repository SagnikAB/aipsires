from flask import Flask, render_template, request, redirect
import os
from werkzeug.utils import secure_filename

from core.resume_parser import extract_text
from core.scoring_engine import score_resume
from core.database import init_db, save_resume, get_all_resumes

app = Flask(__name__)

# Upload folder setup
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Initialize database
init_db()

# ---------------- ROUTES ---------------- #

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    if "resume" not in request.files:
        return redirect("/")

    file = request.files["resume"]

    if file.filename == "":
        return redirect("/")

    # Secure filename to avoid issues
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(filepath)

    # Extract & score
    text = extract_text(filepath)
    score, keywords = score_resume(text)

    # Save to database
    save_resume(filename, score, keywords)

    return render_template("result.html", score=score, keywords=keywords)


@app.route("/history")
def history():
    data = get_all_resumes()
    return render_template("history.html", data=data)


# ---------------- RUN SERVER ---------------- #

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

