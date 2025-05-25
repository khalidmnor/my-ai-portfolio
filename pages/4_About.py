import streamlit as st
import json

st.title("👨‍💻 About Me")
st.write("""
I'm Muhammad Khalid, a senior developer with a passion for AI, backend systems, and mobile-friendly design.
""")

st.write("### ⚙️ Skills")

# Load skills from skills.json
with open("data/skills.json", "r") as f:
    skills = json.load(f)

# Display skills as a word cloud style using markdown and random font sizes/colors
import random

def skill_wordcloud(skills):
    html = ""
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"]
    for skill in skills:
        size = random.randint(16, 32)
        color = random.choice(colors)
        html += f'<span style="font-size:{size}px; color:{color}; margin:8px; display:inline-block;">{skill}</span>'
    st.markdown(f"<div style='line-height:2.5'>{html}</div>", unsafe_allow_html=True)

skill_wordcloud(skills)