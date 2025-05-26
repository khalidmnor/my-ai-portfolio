import streamlit as st
import json
import random

st.title("👨‍💻 About Me")

st.write("""
**Muhammad Khalid Mohd Nor**  
Senior Developer | AI Enthusiast | Backend & Mobile Systems Specialist

Experienced software engineer with a strong background in backend development, AI integration, and mobile-friendly solutions. Passionate about building scalable systems and leveraging AI to solve real-world problems.
""")

st.write("### 🏢 Professional Experience")
st.markdown("""
- **Senior Developer**  
  Led backend and AI projects for various clients, focusing on scalable architectures and robust APIs.
- **AI Integration Specialist**  
  Implemented machine learning models and NLP solutions in production environments.
- **Mobile Systems Developer**  
  Developed cross-platform mobile applications with a focus on performance and usability.
""")

st.write("### ⚙️ Technical Skills")

st.markdown("""
**Programming Languages:**  
Java/JavaEE (JavaEE7, JPA), C/C++, PHP, JSP, PLSQL, SQL (SQL Server, Oracle)

**Web & UI Development:**  
HTML5, AngularJS, GWT, GXT, jQuery, Java, JSP, Oracle, SQL Server, MySQL, RESTful APIs, WebServices, WebSphere, Tomcat, Glassfish

**Data Integration & ETL:**  
Talend Open Studio, SSIS, CodeSmith Generator, ETL pipelines, data lake/warehouse integration, data migration

**Testing & DevOps:**  
Robot Framework, Jenkins, Selenium2Library, Maven, GIT, Subversion, Sonatype Nexus, Redmine

**Reporting & Analytics:**  
JasperReports, Tableau, SQL tuning, data visualization

**System Administration & Infrastructure:**  
Oracle Weblogic, IBM AIX, WebSphere, LDAP, Simple SSO, Linux (RedHat), network inventory, SMS-based task assignment

**Database Management:**  
Oracle 10g/11g, SQL Server, MySQL, SSIS, SQL Tuning, data modeling

**System Integration:**  
Integration with government agencies, financial institutions, and trade logistics
""")

# Skills cloud
st.write("#### 🧩 Skills Cloud")
skills = [
    "Java", "JavaEE", "JPA", "C/C++", "PHP", "JSP", "PLSQL", "SQL", "HTML5", "AngularJS", "GWT", "GXT", "jQuery",
    "RESTful APIs", "WebServices", "WebSphere", "Tomcat", "Glassfish", "Talend", "SSIS", "CodeSmith", "Jenkins",
    "Robot Framework", "Selenium", "Maven", "GIT", "Subversion", "Sonatype Nexus", "Redmine", "JasperReports",
    "Tableau", "Oracle", "SQL Server", "MySQL", "Linux", "LDAP", "AIX"
]

def skill_wordcloud(skills):
    html = ""
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf"]
    for skill in skills:
        size = random.randint(16, 32)
        color = random.choice(colors)
        html += f'<span style="font-size:{size}px; color:{color}; margin:8px; display:inline-block;">{skill}</span>'
    st.markdown(f"<div style='line-height:2.5'>{html}</div>", unsafe_allow_html=True)

skill_wordcloud(skills)

st.write("### 🏅 Certifications & Advanced Training")
st.markdown("""
- **APMG Certified Big Data Professional** (2018)
- **Talend Data Integration (Basics & Advanced)** (2022)
- **Google Professional Cloud Architect** (2024)
- **iTrain Asia Certified Data Science Specialist (CDSS)** (2022)
- **TOGAF 9.2 (Combined Levels 1 & 2)** (2020)
- **XBRL (Fundamental in XBRL)** (2011)
- **JavaEE7 Introduction** (2016)
- **Oracle Database: SQL Tuning for Developers** (2021)
- **Developing Reports with Jaspersoft Studio** (2021)
""")

st.write("### 🧠 Soft Skills")
st.markdown("""
- **Communication:** Proficient in English and Malay; effective collaboration with local and international stakeholders
- **Problem-Solving:** Tackled complex systems (e.g., SQL Server migration, DB storage optimization)
- **Innovation:** Introduced new technologies (Talend, Tableau) to enhance processes and competitiveness
""")

st.write("### 🏢 Industry Experience")
st.markdown("""
- **Government & Financial Sector:** Central Bank of Malaysia, MITI, BNP Paribas, Sumitomo Mitsui, Telekom Malaysia
- **Telecom:** Telekom Malaysia, Celcom (Axiata), National Single Window for Trade (NSW)
""")

st.write("### ⭐ Key Areas of Expertise")
st.markdown("""
- **Java Full Stack:** Backend (Java, JPA, WebServices), Frontend (GWT, GXT, jQuery)
- **ETL & Data Warehousing:** Talend, SSIS, PostgreSQL, data lake integration
- **DevOps & CI/CD:** Jenkins, Maven, GIT, Subversion, CI/CD automation
- **Reporting Tools:** JasperReports, Tableau, XBRL compliance
- **Cloud & Architecture:** Google Cloud Certification, scalable system design

Khalid’s profile highlights a rare blend of technical proficiency, leadership, and specialized knowledge in financial and telecom systems, making him well-suited for roles requiring both hands-on development and strategic oversight.
""")

st.write("### 🌐 Professional Links")
st.markdown("""
- [LinkedIn](https://www.linkedin.com/in/khalidmnor)
- [Email](mailto:khalid.mnor@gmail.com)
""")