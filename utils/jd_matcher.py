import os
from openai import OpenAI
import json

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)

def load_keywords(json_path="data/skills.json"):
    with open(json_path, "r") as f:
        keywords = json.load(f)
    return keywords

def analyze_resume_match_ai(jd_text):
    skills = load_keywords()
    skills_str = ", ".join(skills)
    prompt = (
        f"Given the following job description:\n\n{jd_text}\n\n"
        f"And these skills: {skills_str}\n\n"
        "Evaluate how well the skills match the job description. "
        "Return a match score (0-100) and list the most relevant matched skills."
        "Respond in JSON as: {\"score\": <int>, \"matched_skills\": [<skills>]}"
    )
    response = client.chat.completions.create(
        model="qwen/qwen3-8b:free",
        messages=[{"role": "user", "content": prompt}]
    )
    import re, json as pyjson
    # Extract JSON from response
    try:
        match = re.search(r'\{.*\}', response.choices[0].message.content, re.DOTALL)
        result = pyjson.loads(match.group(0)) if match else {"score": 0, "matched_skills": []}
    except Exception:
        result = {"score": 0, "matched_skills": []}
    return result["score"], result["matched_skills"]