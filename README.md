# ATS-Based Resume Screening & Recruitment Management System

## Overview

An AI-powered Applicant Tracking System (ATS) developed using Python, PostgreSQL, and Streamlit to automate resume screening, candidate evaluation, and recruitment analytics.

## Features

* Resume Upload through Streamlit
* PDF Resume Parsing
* Candidate Name Extraction
* Skill Extraction
* ATS Score Calculation
* Missing Skill Analysis
* PostgreSQL Integration
* Candidate Ranking Dashboard
* KPI Metrics
* ATS Score Visualization
* Candidate Submission Workflow

## Tech Stack

* Python
* PostgreSQL
* Streamlit
* Pandas
* pdfplumber
* psycopg2
* Plotly
* Scikit-Learn

## Database Schema

### Candidates

```sql
candidate_id
name
email
phone
resume_text
```

### Jobs

```sql
job_id
job_title
required_skills
min_experience
```

### Candidate Scores

```sql
score_id
candidate_name
job_title
ats_score
matched_skills
missing_skills
created_at
```

## Installation

```bash
git clone https://github.com/yourusername/ATS-Resume-Screener.git

cd ATS-Resume-Screener

pip install -r requirements.txt

streamlit run dashboard.py
```

## Dashboard Features

* Candidate Rankings
* ATS Score Analysis
* Resume Upload
* Skill Gap Analysis
* Top Candidate Identification
* Hiring Analytics

## Future Enhancements

* Multiple Job Selection
* Resume Recommendation Engine
* PDF Report Generation
* Candidate Leaderboard
* LLM Integration
* Interview Question Generator
