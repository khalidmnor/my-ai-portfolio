import streamlit as st
import json

st.title("Projects")

with open("data/projects.json") as f:
    projects = json.load(f)

for p in projects:
    st.subheader(p["title"])
    st.caption(f"Tech Stack: {p['tech']}")
    st.write(p["summary"])
