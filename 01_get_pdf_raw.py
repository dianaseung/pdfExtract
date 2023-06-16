#!/usr/bin/env python3

# Import required library.
import pdfplumber

# Open the file and create a pdf object.
pdf = pdfplumber.open("input.pdf")

# Get and Print the number of pages.
numPages = len(pdf.pages)
print("Number of Pages:", numPages)

# Iterate over each page and extract the text of each page.
for number, pageText in enumerate(pdf.pages):
    output = './output/raw_pdf_extract.txt'
    print("Page Number:", number, file=open(output, 'a'))
    print(pageText.extract_text(), file=open(output,'a'))
    # print("==================================================", file=open('./output/raw_extract.txt', 'a'))