#!/usr/bin/env python3

# Import required library.
import pdfplumber
from os import path

# Define Output File
raw_output = './output/raw_pdf_extract.txt'

# Define Input Directory /  File
# file_input = './input/input.pdf'
file_input = input('Enter path to input file: ')

while path.isfile(file_input) == False:
    "Invalid file: "+str(file_input)
    file_input = input
else:
    # Open the file and create a pdf object.
    pdf = pdfplumber.open(file_input)

    # Get and Print the number of pages.
    numPages = len(pdf.pages)
    print("Number of Pages:", numPages)

    # Iterate over each page and extract the text of each page.
    for number, pageText in enumerate(pdf.pages):
        print("Page Number:", number, file=open(raw_output, 'a'))
        print(pageText.extract_text(), file=open(raw_output,'a'))
    print("SUCCESS: Text extracted from", file_input, "to", raw_output)