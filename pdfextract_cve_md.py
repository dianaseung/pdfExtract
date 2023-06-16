#!/usr/bin/env python3
# Compiled one-step script to extract CVEs from a PDF and prepare them with markdown

# Import required library.
import pdfplumber
import re
import os

# Open the file and create a pdf object.
pdf = pdfplumber.open("input.pdf")

# Get and Print the number of pages.
numPages = len(pdf.pages)
print("Number of Pages:", numPages)

# Iterate over each page and extract the raw text of each page in the PDF to txt.
raw_output = './output/raw_pdf_extract.txt'
for number, pageText in enumerate(pdf.pages):
    # Define the raw text output file
    print("Page Number:", number, file=open(raw_output, 'a'))
    print(pageText.extract_text(), file=open(raw_output,'a'))

# This extracts only the CVEs from a raw_output
cve_output = './output/cve_extract.txt'
with open (raw_output, 'rt') as pdf_extract:
    for line in pdf_extract:
        regex = r'CVE-\d{4,5}-\d{4,7}'
        regex_find = re.compile(regex)
        result = regex_find.findall(line)
        if result:
            for x in result:
                print(x, file=open(cve_output, 'a'))

# This reformats a txt list of CVEs into a Markdown-compatible list with NVD links
with open (cve_output, 'rt') as cve_list:
    for cve in cve_list:
        cleaned_cve = cve.strip().replace(' ', '')
        md_start = '['
        md_url  = '|https://nvd.nist.gov/vuln/detail/'
        md_end = ']'
        print(md_start.strip(), cleaned_cve.strip(), md_url.strip(), cleaned_cve.strip(), md_end.strip(), sep="", file=open('./output/md_cve_list.txt','a'))