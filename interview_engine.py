from sentence_transformers import SentenceTransformer, util
import random

model = SentenceTransformer('all-MiniLM-L6-v2')

QUESTION_BANK = {
 "python": ["Explain decorators", "What is GIL?"],
 "sql": ["What is normalization?", "Explain joins"],
 "ml": ["What is overfitting?", "Bias vs Variance"]
}

def generate_question(skills):
    if not skills:
        return "Introduce yourself."
    skill = random.choice(skills)
    return random.choice(QUESTION_BANK.get(skill, ["Describe a project."]))

def evaluate_answer(answer, expected="good answer"):
    emb1 = model.encode(answer)
    emb2 = model.encode(expected)
    score = util.cos_sim(emb1, emb2).item()
    return round(score * 100, 2)
