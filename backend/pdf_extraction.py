# Requirements: Modules - pdfminer.six, PyMUPDF, pillow,

# Text extraction
# pip install pdfminer.six

# Image extraction
# pip install PyMUPDF
# pip install pillow

# Tabular Data extraction
# pip install tabula
# pip install tabula-py --upgrade

from pdfminer.high_level import extract_pages, extract_text

# Text extraction

text = extract_text("C:/Users/ajjos/OneDrive/Desktop/EduBot/backend/test.pdf")
print(text)
print("\n\n")

# Element extraction

for page_layout in extract_pages(
    "C:/Users/ajjos/OneDrive/Desktop/EduBot/backend/test.pdf"
):
    for element in page_layout:
        print(element)

# Image extraction

import fitz
import PIL.Image
import io

pdf = fitz.open("C:/Users/ajjos/OneDrive/Desktop/EduBot/backend/test.pdf")
counter = 1
for i in range(len(pdf)):
    page = pdf[i]
    images = page.get_images()
    for image in images:
        base_img = pdf.extract_image(image[0])
        image_data = base_img["image"]
        img = PIL.Image.open(io.BytesIO(image_data))
        extension = base_img["ext"]
        img.save(open(f"iamge{counter}.{extension}", "wb"))
        counter += 1

# Tabular data extraction

import tabula

tables = tabula.read_pdf(
    "C:/Users/ajjos/OneDrive/Desktop/EduBot/backend/table_test.pdf", pages="all"
)
print(tables)
