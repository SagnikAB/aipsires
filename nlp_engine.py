import spacy
from spacy.matcher import PhraseMatcher

nlp = spacy.load("en_core_web_sm")

SKILLS = [
 "python","java","machine learning","deep learning",
 "sql","flask","django","html","css","react","node"
]

matcher = PhraseMatcher(nlp.vocab)
patterns = [nlp(skill) for skill in SKILLS]
matcher.add("SKILLS", patterns)

def extract_skills(text):
    doc = nlp(text.lower())
    matches = matcher(doc)
    found = set()
    for _, start, end in matches:
        found.add(doc[start:end].text)
    return list(found)
