from flask import Flask, render_template, request, redirect
import os
from core.resume_parser import extract_text
from core.scoring_engine import score_resume
from core.database import init_db, save_resume, get_all_resumes

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Initialize database
init_db()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    if "resume" not in request.files:
        return redirect("/")

    file = request.files["resume"]
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    text = extract_text(filepath)
    score, keywords = score_resume(text)

    # Save to database
    save_resume(file.filename, score, keywords)

    return render_template("result.html", score=score, keywords=keywords)

@app.route("/history")
def history():
    data = get_all_resumes()
    return render_template("history.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
