from parser.pdf_parser import extract_text
from parser.name_extractor import extract_name

text = extract_text("resumes/Parthasarathi_Mohanty_Resume.pdf")

name = extract_name(text)

print("NAME:", name)