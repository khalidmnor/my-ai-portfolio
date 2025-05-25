import streamlit as st
import json
import os

st.title("🔐 Admin Panel")

# Disable screen based on environment variable
if os.getenv("ADMIN_DISABLED", "false").lower() == "true":
    st.warning("Admin panel is disabled.")
    st.stop()

# Load existing projects
try:
    with open("data/projects.json", "r") as f:
        projects = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    projects = []

# Load existing skills
try:
    with open("data/skills.json", "r") as f:
        skills = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    skills = []

# Display existing projects with edit option
st.subheader("Existing Projects")
for idx, proj in enumerate(projects):
    with st.expander(f"{proj['title']}"):
        new_title = st.text_input(f"Edit Title {idx}", value=proj['title'], key=f"title_{idx}")
        new_tech = st.text_input(f"Edit Tech Stack {idx}", value=proj['tech'], key=f"tech_{idx}")
        new_summary = st.text_area(f"Edit Summary {idx}", value=proj['summary'], key=f"summary_{idx}")
        if st.button(f"Save Changes {idx}"):
            projects[idx] = {"title": new_title, "tech": new_tech, "summary": new_summary}
            with open("data/projects.json", "w") as f:
                json.dump(projects, f, indent=4)
            st.success("Project updated!")

st.subheader("Add New Project")
title = st.text_input("Project Title")
tech = st.text_input("Tech Stack")
summary = st.text_area("Summary")

if st.button("Add Project"):
    new_proj = {"title": title, "tech": tech, "summary": summary}
    projects.append(new_proj)
    with open("data/projects.json", "w") as f:
        json.dump(projects, f, indent=4)
    st.success("Project added!")

# --- Skills Admin Section ---
st.subheader("Manage Skills")

# Display and remove skills
for idx, skill in enumerate(skills):
    cols = st.columns([6, 1])
    cols[0].write(skill)
    if cols[1].button("❌", key=f"remove_skill_{idx}"):
        skills.pop(idx)
        with open("data/skills.json", "w") as f:
            json.dump(skills, f, indent=4)
        st.success(f"Removed skill: {skill}")
        st.experimental_rerun()

# Add new skill
new_skill = st.text_input("Add New Skill")
if st.button("Add Skill"):
    if new_skill and new_skill not in skills:
        skills.append(new_skill)
        with open("data/skills.json", "w") as f:
            json.dump(skills, f, indent=4)
        st.success(f"Added skill: {new_skill}")
        st.experimental_rerun()
    elif new_skill in skills:
        st.warning("Skill already exists.")