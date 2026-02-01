# 🤖 AI-Powered Smart Interview & Resume Evaluation System

An intelligent, machine learning–driven recruitment support system that automates **resume screening** and **interview evaluation** using **Natural Language Processing (NLP)** techniques.  
The system aims to provide **objective, scalable, and data-driven candidate assessment**, reducing manual effort and human bias in hiring processes.

---

## 📖 Overview
Recruitment processes traditionally rely on manual resume screening and subjective interview evaluations, which are time-consuming and prone to inconsistency.  
This project proposes an **AI-powered system** that evaluates candidates based on:
- Resume relevance
- Skill matching
- Interview response quality  

By leveraging **Machine Learning and NLP**, the system ensures consistent and unbiased candidate evaluation.

---

## ❓ Problem Statement
Current hiring processes suffer from:
- Manual and repetitive resume screening
- Subjective interview assessments
- Difficulty in scaling for large applicant pools
- Inconsistent decision-making across recruiters

---

## 🎯 Objectives
- Automate resume screening using ML techniques  
- Evaluate interview responses using NLP  
- Reduce bias and subjectivity in candidate selection  
- Rank candidates based on overall suitability  
- Provide a scalable and extensible hiring framework  

---

## 🔄 System Workflow
1. Candidate uploads resume (PDF/DOC)
2. Resume text extraction and preprocessing
3. Feature extraction using NLP
4. ML-based resume scoring
5. AI-assisted interview (text-based)
6. Interview response evaluation
7. Final candidate score and ranking

---

## ✨ Key Features
- 📄 Automated resume parsing
- 🧠 Machine learning–based resume scoring
- 💬 NLP-based interview answer evaluation
- 📊 Candidate ranking and analytics
- ⚖ Objective and bias-reduced assessment
- 🔌 Modular architecture for future upgrades

---

## 🧠 Machine Learning & NLP Approach

### Resume Evaluation
- Text preprocessing: tokenization, stopword removal, lemmatization
- Feature extraction: TF-IDF vectors
- Models used:
  - Logistic Regression
  - Support Vector Machine (SVM)
  - Random Forest
- Output:
  - Resume relevance score
  - Skill match percentage

### Interview Evaluation
- Semantic similarity between candidate answers and ideal answers
- Keyword relevance analysis
- Sentiment analysis for clarity and confidence estimation

---

## 🛠 Tech Stack

| Layer | Technology |
|-----|-----------|
| Programming Language | Python |
| Backend Framework | Flask |
| Machine Learning | Scikit-learn |
| NLP | NLTK, SpaCy |
| Frontend | HTML, CSS, JavaScript |
| Database | SQLite / MongoDB |
| Tools | Git, GitHub |

---

## 📂 Dataset
- Public resume datasets (Kaggle)
- Custom interview question–answer dataset
- Synthetic candidate profiles for testing and experimentation

---

## ⚙ Installation & Setup

### 1️⃣ Clone the Repository
bash
git clone https://github.com/Sambit1110/AI-Powered-Smart-Interview-Resume-Evaluation-System.git
cd AI-Powered-Smart-Interview-Resume-Evaluation-System

### 2️⃣ Create Virtual Environment
bash
python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate

### 3️⃣ Install Dependencies
bash
pip install -r requirements.txt

### 4️⃣ Run the Application
bash
python app.py

## AI-Powered-Smart-Interview-Resume-Evaluation-System/
│
├── data/
│   ├── resumes/
│   └── interview_data/
│
├── models/
│   ├── resume_model.pkl
│   └── interview_model.pkl
│
├── preprocessing/
│   ├── resume_parser.py
│   └── text_cleaner.py
│
├── training/
│   ├── train_resume_model.py
│   └── train_interview_model.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   └── js/
│
├── app.py
├── requirements.txt
└── README.md

## 🔬 Research & Development Aspect
1. Comparative study of multiple ML models
2. Feature engineering experimentation
3. Evaluation using accuracy, precision, recall, and F1-score
4. Bias reduction through objective scoring mechanisms
5. Modular design for extensible AI research

## 📊 Results & Observations
1. Improved consistency in resume screening
2. Accurate relevance scoring for candidate profiles
3. Reduced manual screening effort
4. Effective interview response evaluation using NLP similarity metrics

## 📜 License

This project is licensed under the MIT License.
You are free to use, modify, and distribute this project with proper attribution.
