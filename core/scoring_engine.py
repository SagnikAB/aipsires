KEYWORDS = [
    "python", "java", "sql", "flask", "django",
    "machine learning", "ai", "data", "git",
    "html", "css", "javascript"
]

def score_resume(text):
    found = []
    score = 0

    for word in KEYWORDS:
        if word in text:
            score += 10
            found.append(word)

    score = min(score, 100)
    return score, found
