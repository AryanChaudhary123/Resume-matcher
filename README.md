# 🧠 Resume Matcher with Keyword Visualization

A smart and interactive web-based tool that helps recruiters and hiring managers automatically rank resumes based on their relevance to a given job description — with **highlighted keyword matches** for enhanced clarity and decision-making.

---

## 🚀 Demo
![image](https://github.com/user-attachments/assets/5fd277aa-5d3d-413c-b75f-3db572987224)

![image](https://github.com/user-attachments/assets/f9cd79a8-5c1a-4ca2-bbb3-2fed7d3ba59b)

![image](https://github.com/user-attachments/assets/85f43e62-d3e1-451a-b7de-2b54e614c5ea)


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
# Project Structure
resume-matcher/
├── main.py                  # Core Flask app with matching logic
├── templates/
│   └── matchresume.html     # Web interface (form + results)
├── uploads/                 # Stores uploaded resume files
├── static/                  # (Optional) for custom CSS or assets
└── README.md

