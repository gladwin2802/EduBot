import re
from pdfminer.high_level import extract_pages, extract_text

text = extract_text("C:/Users/ajjos/OneDrive/Desktop/EduBot/backend/test.pdf")
print(text)
print("\n\n")
for page_layout in extract_pages("C:/Users/ajjos/OneDrive/Desktop/EduBot/backend/test.pdf"):
    for element in page_layout:
        print(element)
    