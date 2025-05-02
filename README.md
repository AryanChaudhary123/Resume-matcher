# 🧠 Resume Matcher with Keyword Visualization

A smart and interactive web-based tool that helps recruiters and hiring managers automatically rank resumes based on their relevance to a given job description — with **highlighted keyword matches** for enhanced clarity and decision-making.

---

## 🚀 Demo

> Upload multiple resumes and enter a job description to get the top matching candidates with important keywords visually highlighted for transparency.

---

## ✨ Features

- 📄 **Supports Multiple Formats**: Upload resumes in PDF, DOCX, or TXT format.
- 🧠 **Intelligent Matching**: Uses TF-IDF (Term Frequency-Inverse Document Frequency) and cosine similarity to score and rank resumes.
- 💡 **Keyword Visualization**: Matched keywords from the job description are highlighted in the resume text.
- 📊 **Top Resume Ranking**: Displays the top 5 most relevant resumes with similarity scores.
- 🖥️ **Clean Frontend UI**: Minimalist and responsive web interface using Flask and HTML/CSS.
- 🔒 **Local-First Processing**: All matching and file processing occurs on your machine—no third-party APIs or uploads.

---

## 🛠️ Tech Stack

| Layer         | Technology              |
|---------------|--------------------------|
| Frontend      | HTML, CSS                |
| Backend       | Python (Flask)           |
| NLP / Matching| scikit-learn (TF-IDF, Cosine Similarity) |
| File Handling | PyPDF2, docx2txt         |
| Deployment    | Flask (local server)     |

---

