#!/usr/bin/env python3
# Compiled one-step script to extract CVEs from a PDF and prepare them with markdown

# Import required library.
import pdfplumber
import re
import os
from os import path

# Define raw PDF text Output File
raw_output = './output/raw_pdf_extract.txt'

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

# Define CVE list Output File
cve_output = './output/cve_extract.txt'

# This extracts only the CVEs from a raw_output
with open (raw_output, 'rt') as pdf_extract:
    for line in pdf_extract:
        regex = r'CVE-\d{4,5}-\d{4,7}'
        regex_find = re.compile(regex)
        result = regex_find.findall(line)
        if result:
            for x in result:
                print(x, file=open(cve_output, 'a'))
    print("SUCCESS: List of CVE extracted to", cve_output)

# This reformats a txt list of CVEs into a Markdown-compatible list with NVD links
with open (cve_output, 'rt') as cve_list:
    for cve in cve_list:
        cleaned_cve = cve.strip().replace(' ', '')
        md_start = '# ['
        md_url  = '|https://nvd.nist.gov/vuln/detail/'
        md_end = ']'
        print(md_start.strip(), cleaned_cve.strip(), md_url.strip(), cleaned_cve.strip(), md_end.strip(), sep="", file=open('./output/md_cve_list.txt','a'))
    print("SUCCESS: Markdown format complete!")