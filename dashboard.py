import streamlit as st
from database import insert_score
from database.job_loader import get_job
from matching_engine.scorer import calculate_match_score
import pandas as pd
from database.db_connection import conn
import tempfile
from parser.pdf_parser import extract_text
from parser.skill_extractor import extract_skills
from database.insert_score import insert_score
from parser.name_extractor import extract_name

st.set_page_config(
    page_title="AI Resume Screener",
    layout="wide"
)

st.title("📄 AI Resume Screening Dashboard")
uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)
if uploaded_file is not None:

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as tmp_file:

        tmp_file.write(
            uploaded_file.getbuffer()
        )

        pdf_path = tmp_file.name

    text = extract_text(pdf_path)
    
    candidate_name = extract_name(text)
    
    st.subheader("Candidate Name")
    st.write(candidate_name)


    st.subheader("Resume Preview")
    st.text(text[:1000])

    candidate_skills = extract_skills(text)

    st.subheader("Extracted Skills")
    st.write(candidate_skills)

    job_title, required_skills = get_job(1)

    job_skills = [
        skill.strip()
        for skill in required_skills.split(",")
    ]

    score, matched, missing = calculate_match_score(
        candidate_skills,
        job_skills
    )

    st.subheader("ATS Analysis")

    st.metric(
        "ATS Score",
        f"{score}%"
    )
    if score >= 90:
        st.success(
        f"Excellent Match! ATS Score: {score}%"
    )

    elif score >= 70:
        st.warning(
            f"Good Match! ATS Score: {score}%"
        )
    

    else:
        st.error(
        f"Needs Improvement! ATS Score: {score}%"
    )
    

    st.write("✅ Matched Skills:")
    st.write(matched)

    st.write("❌ Missing Skills:")
    st.write(missing)
    if st.button("Submit Candidate"):

        insert_score(
        candidate_name,
        job_title,
        score,
        matched,
        missing
    )

    st.success("Candidate Saved Successfully!")


query = """
SELECT
    candidate_name,
    job_title,
    ats_score,
    matched_skills,
    missing_skills,
    created_at
FROM candidate_scores
ORDER BY ats_score DESC
"""

df = pd.read_sql(query, conn)

# KPI Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Candidates", len(df))

with col2:
    st.metric(
        "Highest ATS Score",
        f"{df['ats_score'].max()}%"
    )

with col3:
    st.metric(
        "Average ATS Score",
        f"{round(df['ats_score'].mean(), 2)}%"
    )

# Table
st.subheader("Candidate Rankings")
st.dataframe(df, use_container_width=True)

# Top Candidate
st.subheader("🏆 Top Candidate")

if not df.empty:

    top = df.iloc[0]

    st.success(
        f"{top['candidate_name']} scored {top['ats_score']}%"
    )

    st.write(
        "Matched Skills:",
        top["matched_skills"]
    )

    st.write(
        "Missing Skills:",
        top["missing_skills"]
    )

# 👇 PASTE THE NEW CHART CODE HERE

st.subheader("📊 ATS Score Comparison")

chart_df = df[
    ["candidate_name", "ats_score"]
]

st.bar_chart(
    chart_df.set_index(
        "candidate_name"
    )
)