from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def score_resume(resume_text, job_desc):
    docs = [resume_text, job_desc]
    tfidf = TfidfVectorizer(stop_words='english')
    matrix = tfidf.fit_transform(docs)
    similarity = cosine_similarity(matrix[0:1], matrix[1:2])[0][0]
    return round(similarity * 100, 2)
