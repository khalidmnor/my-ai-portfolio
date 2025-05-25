import streamlit as st
from utils.jd_matcher import analyze_resume_match_ai

st.title("📄 Resume Match")

jd_file = st.file_uploader("Upload Job Description", type=["pdf", "txt"])
jd_text = ""
if jd_file:
    if jd_file.name.endswith(".txt"):
        jd_text = jd_file.read().decode("utf-8")
    elif jd_file.name.endswith(".pdf"):
        import PyPDF2
        reader = PyPDF2.PdfReader(jd_file)
        jd_text = ""
        for page in reader.pages:
            jd_text += page.extract_text() or ""
    if jd_text:
        with st.spinner("Analyzing with AI..."):
            match_score, matched_skills = analyze_resume_match_ai(jd_text)
        st.subheader("Match Score")
        st.progress(match_score / 100)
        st.write(f"**{match_score}%**")
        st.subheader("Matched Skills / Keywords")
        if matched_skills:
            for kw in matched_skills:
                st.success(kw)
        else:
            st.info("No keywords matched.")
        st.divider()
        st.subheader("Job Description Preview")
        st.code(jd_text[:1500] + ("..." if len(jd_text) > 1500 else ""), language="markdown")
    else:
        st.warning("Could not extract text from the uploaded file.")