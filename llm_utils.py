# llm_utils.py
import os
import re
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def load_prompt(template_file: str, **kwargs) -> str:
    with open(template_file, "r") as file:
        prompt = file.read()
    for key, value in kwargs.items():
        prompt = prompt.replace(f"{{{{{key}}}}}", value)
    return prompt

def get_resume_feedback(resume_text: str) -> str:
    prompt = load_prompt("prompts/resume_feedback.txt", RESUME_TEXT=resume_text)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    return response.choices[0].message.content

def get_jd_match_score(resume_text: str, jd_text: str) -> tuple:
    prompt = load_prompt("prompts/jd_match_prompt.txt", RESUME_TEXT=resume_text, JD_TEXT=jd_text)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    content = response.choices[0].message.content
    match = re.search(r"(\\d{1,3})/100", content)
    score = int(match.group(1)) if match else 0
    return score, content
