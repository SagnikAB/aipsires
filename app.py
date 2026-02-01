from flask import Flask, request, render_template
from nlp_engine import extract_skills
from scoring_engine import score_resume
from interview_engine import generate_question, evaluate_answer
from database import init_db, insert_candidate

app = Flask(__name__)
init_db()

@app.route("/", methods=["GET","POST"])
def index():
    result = None
    if request.method == "POST":
        resume = request.form["resume_text"]
        job_desc = request.form["job_desc"]

        skills = extract_skills(resume)
        r_score = score_resume(resume, job_desc)
        question = generate_question(skills)

        answer = request.form.get("answer","")
        i_score = evaluate_answer(answer)

        insert_candidate("User", r_score, i_score)

        result = {
            "skills": skills,
            "resume_score": r_score,
            "interview_score": i_score,
            "question": question
        }

    return render_template("index.html", result=result)

app.run(debug=True)
