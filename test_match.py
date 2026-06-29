from matching_engine.scorer import calculate_match_score

candidate_skills = [
    "python",
    "sql",
    "power bi",
    "excel"
]

job_skills = [
    "python",
    "sql",
    "power bi",
    "excel",
    "pandas"
]

score, matched = calculate_match_score(
    candidate_skills,
    job_skills
)

print("Score:", score)
print("Matched Skills:", matched)