from parser.pdf_parser import extract_text
from parser.info_extractor import extract_email, extract_phone
from parser.skill_extractor import extract_skills
from parser.name_extractor import extract_name
from database.insert_candidate import insert_candidate

pdf_path = "resumes/Parthasarathi_Mohanty_Resume.pdf"  # Replace with your resume file

text = extract_text(pdf_path)

name = extract_name(text)
email = extract_email(text)
phone = extract_phone(text)
skills = extract_skills(text)

print("\n===== CANDIDATE DETAILS =====")
print("Name:", name)
print("Email:", email)
print("Phone:", phone)
print("Skills:", skills)

insert_candidate(
    name,
    email,
    phone,
    text
)

print("Name:", name)
print("Email:", email)
print("Phone:", phone)
print("Skills:", skills)
