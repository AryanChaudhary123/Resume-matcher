from flask import Flask, request, render_template
import os
import docx2txt
import PyPDF2
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text 

def extract_text_from_docx(file_path):
    return docx2txt.process(file_path)                

def extract_text_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def extract_text(file_path):
    if file_path.endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith('.docx'):
        return extract_text_from_docx(file_path)
    elif file_path.endswith('.txt'):
        return extract_text_from_txt(file_path)
    else:
        return ""

@app.route("/")
def matchresume():
    return render_template('matchresume.html')

@app.route('/matcher', methods=['POST'])
def matcher():
    if request.method == 'POST':
        job_description = request.form['job_description']
        resume_files = request.files.getlist('resumes')

        resumes = []
        raw_texts = []
        for resume_file in resume_files:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], resume_file.filename)
            resume_file.save(filename)
            text = extract_text(filename)
            resumes.append(text)
            raw_texts.append(text)

        if not resumes or not job_description:
            return render_template('matchresume.html', message="Please upload resumes and enter a job description.")

        vectorizer = TfidfVectorizer().fit([job_description] + resumes)
        vectors = vectorizer.transform([job_description] + resumes).toarray()

        job_vector = vectors[0]
        resume_vectors = vectors[1:]
        similarities = cosine_similarity([job_vector], resume_vectors)[0]

        top_indices = similarities.argsort()[-5:][::-1]
        matched_info = []

        job_keywords = set(vectorizer.get_feature_names_out())

        for i in top_indices:
            text = raw_texts[i]
            tokens = text.lower().split()
            matches = [word for word in tokens if word in job_keywords]

            # Highlight matched keywords
            highlighted = ' '.join([
                f"<span style='background-color: #d4edda; color: #155724; font-weight: bold'>{word}</span>"
                if word in job_keywords else word for word in tokens
            ])

            matched_info.append({
                "filename": resume_files[i].filename,
                "score": round(similarities[i], 2),
                "highlighted_resume": highlighted
            })

        return render_template('matchresume.html',
                               message="Top matching resumes with matched keywords highlighted:",
                               matched_info=matched_info)

    return render_template('matchresume.html')

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)