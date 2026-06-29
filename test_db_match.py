from parser.pdf_parser import extract_text
from parser.skill_extractor import extract_skills
from database.insert_score import insert_score
from database.job_loader import get_job
from matching_engine.scorer import calculate_match_score

text = extract_text(
    "resumes/Parthasarathi_Mohanty_Resume.pdf"
)

candidate_skills = extract_skills(text)

job_title, required_skills = get_job(1)

job_skills = [
    skill.strip()
    for skill in required_skills.split(",")
]

score, matched, missing = calculate_match_score(
    candidate_skills,
    job_skills
)

insert_score(
    "Parthasarathi Mohanty",
    job_title,
    score,
    matched,
    missing
)

print("\nJOB:", job_title)
print("Candidate Skills:", candidate_skills)
print("Required Skills:", job_skills)
print("Matched Skills:", matched)
print("Missing Skills:", missing)
print("ATS Score:", score, "%")