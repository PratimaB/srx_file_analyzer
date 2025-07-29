# app.py
import streamlit as st
from resume_parser import extract_resume_text
from job_description_parser import get_jd_text
from llm_utils import get_resume_feedback, get_jd_match_score

st.set_page_config(page_title="LLM Resume Analyzer", layout="wide")
st.title("📄 LLM-Powered Resume Analyzer")

st.sidebar.header("Upload Resume and Job Description")
resume_file = st.sidebar.file_uploader("Upload your Resume (PDF)", type=["pdf"])

jd_text = st.sidebar.text_area("Paste Job Description Here", height=200)

if resume_file:
    with st.spinner("Parsing resume..."):
        resume_text = extract_resume_text(resume_file)

    st.subheader("Extracted Resume Text")
    st.text_area("", resume_text, height=200)

    if st.button("🔍 Analyze Resume"):
        with st.spinner("Generating feedback..."):
            feedback = get_resume_feedback(resume_text)
        st.subheader("📝 Resume Feedback")
        st.write(feedback)

    if jd_text and st.button("🤝 Match with Job Description"):
        with st.spinner("Matching with job description..."):
            match_score, match_feedback = get_jd_match_score(resume_text, jd_text)
        st.subheader("🎯 Match Score")
        st.write(f"**Score:** {match_score}/100")
        st.write(match_feedback)
else:
    st.info("Please upload your resume (PDF) to begin.")
