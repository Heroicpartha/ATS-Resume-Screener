SKILLS_DB = [
    "python",
    "sql",
    "postgresql",
    "mysql",
    "power bi",
    "tableau",
    "excel",
    "pandas",
    "numpy",
    "machine learning",
    "deep learning",
    "javascript",
    "react",
    "nodejs",
    "html",
    "css",
    "c++",
    "java"
]

def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS_DB:

        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))