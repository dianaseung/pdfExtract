#!/usr/bin/env python3

# Import required library.
import pdfplumber
from os import path

# Define Output File
raw_output = './output/01_raw_pdf_extract.txt'

# Define Input Directory /  File
file_input = input('[Enter path to PDF file]: ')

input_name, input_extension = path.splitext(file_input)

while (path.isfile(file_input) == False) or (input_extension.lower() != '.pdf'):
    print("ERROR: Invalid file -", file_input, "(extension:", input_extension, ")\n")
    file_input = input('[Enter valid path to PDF file]: ')
    input_name, input_extension = path.splitext(file_input)
    print("INFO: New input file -", file_input, "(extension:", input_extension, ")")
else:
    # Open the file and create a pdf object.
    pdf = pdfplumber.open(file_input)

    # Get and Print the number of pages.
    numPages = len(pdf.pages)
    print("INFO: Extracting", numPages, "pages of raw text from", file_input, "(extension:", input_extension, ")")

    # Iterate over each page and extract the text of each page.
    for number, pageText in enumerate(pdf.pages):
        print("Page Number:", number, file=open(raw_output, 'a'))
        print(pageText.extract_text(), file=open(raw_output,'a'))
    print("SUCCESS: Text extracted from", file_input, "to", raw_output)