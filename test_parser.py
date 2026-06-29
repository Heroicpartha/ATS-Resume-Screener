from parser.pdf_parser import extract_text
from parser.info_extractor import extract_email, extract_phone
from parser.skill_extractor import extract_skills

text = extract_text(
    "resumes/Parthasarathi_Mohanty_Resume.pdf"
)

print("EMAIL:", extract_email(text))
print("PHONE:", extract_phone(text))

print("SKILLS:")
print(extract_skills(text))