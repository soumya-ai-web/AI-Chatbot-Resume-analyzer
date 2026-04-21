import streamlit as st
import PyPDF2

st.set_page_config(page_title="AI Resume Analyzer PRO", page_icon="🤖")

st.title("🤖 AI Resume Analyzer PRO")
st.write("Upload your resume and get smart analysis 🔥")

uploaded_file = st.file_uploader("📄 Upload Resume (PDF)", type="pdf")

if uploaded_file:
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content

    st.subheader("📑 Resume Preview")
    st.write(text[:1200])

    # Skills
    skills = []
    keywords = ["python", "java", "sql", "html", "css", "machine learning", "ai", "data science"]

    for word in keywords:
        if word in text.lower():
            skills.append(word.title())

    st.subheader("🧠 Skills Found")
    st.write(", ".join(skills) if skills else "No major skills detected")

    # Score
    score = len(skills) * 12
    if score > 100:
        score = 100

    st.subheader("📊 Resume Score")
    st.progress(score)
    st.write(f"Score: {score}/100")

    # Jobs
    st.subheader("💼 Suggested Jobs")

    if "Python" in skills or "Ai" in skills:
        st.write("• AI Intern")
        st.write("• Python Developer")

    if "Sql" in skills:
        st.write("• Data Analyst")

    if "Html" in skills or "Css" in skills:
        st.write("• Web Developer")

    # Tips
    st.subheader("📈 Improvement Tips")
    st.write("✔ Add Projects")
    st.write("✔ Add Internship Experience")
    st.write("✔ Add Certifications")
    st.write("✔ Use clean formatting")

    st.success("Analysis Complete 🎉")
