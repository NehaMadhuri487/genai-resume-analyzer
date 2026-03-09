# AI Resume Analyzer

An AI-powered resume analysis tool that evaluates resumes using ATS-style scoring and provides actionable feedback for job seekers.

Built using Python, Streamlit, and LLM APIs.

---

## Features

* Upload resume in PDF format
* ATS score evaluation
* Automatic skill detection
* Recommended job roles
* Resume strengths analysis
* Weakness identification
* Suggestions for improvement

---

## Tech Stack

* Python
* Streamlit
* PyPDF2
* OpenRouter API
* LLM Model (Llama / Mistral)

---


##Project structure
app.py
ai_analyzer.py
ats_score.py
pdf_parser.py  
requirements.txt

## Installation

Clone the repository:

```
git clone https://github.com/your-username/ai-resume-analyzer.git
```

Go to the project folder:

```
cd ai-resume-analyzer
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Run the Application

Start the Streamlit app:

```
streamlit run app.py
```

The application will open in your browser.

---

## How It Works

1. Upload a resume in PDF format.
2. The system extracts text using PyPDF2.
3. The resume text is sent to an LLM via OpenRouter API.
4. The AI analyzes the resume and generates:

   * ATS score
   * Skills detected
   * Recommended roles
   * Strengths
   * Weaknesses
   * Improvement suggestions.

---

## Future Improvements

* Job description matching
* Resume-job compatibility score
* Missing skills detection
* Resume analytics dashboard
* Downloadable analysis report

---

## Author

Developed as an AI project using Python and Streamlit.
