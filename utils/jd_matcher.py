import json

def load_keywords(json_path="data/skills.json"):
    with open(json_path, "r") as f:
        keywords = json.load(f)
    return keywords

def analyze_resume_match(jd_text):
    keywords = load_keywords()
    if not keywords:
        return 0, ""
    print(f"Loaded {len(keywords)} keywords for matching.")
    score = sum(k.lower() in jd_text.lower() for k in keywords) / len(keywords) * 100
    highlights = ", ".join([k for k in keywords if k.lower() in jd_text.lower()])
    return int(score), highlights