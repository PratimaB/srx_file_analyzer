# srx_file_analyzer
Overview
Build a Python web app that uses a large language model (like OpenAI's GPT) to analyze a user's resume and:

Suggest improvements

Extract skills and experience

Match the resume against job descriptions

**#Tech Stack**
Frontend: Streamlit (for fast UI prototyping)

Backend: Python

LLM API: OpenAI GPT-4 (or use transformers with a local model if no API)

PDF Parsing: PyMuPDF or pdfplumber

Job Description Parsing: Text matching + GPT semantic comparison

**Core Features**

Upload Resume (PDF)

Parse Resume Text

LLM Feedback Generator – Returns suggestions to improve structure, grammar, clarity, and ATS-friendliness.

Skill Extractor – Identifies skills using NER or LLM.

Job Description Matching

User pastes JD text.

LLM evaluates how well the resume matches the JD.

Score out of 100 + recommended updates.
