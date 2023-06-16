# __init__.py

# Import required library.
import pdfplumber
import re
import os
from os import path

# Define raw PDF text Output File
raw_output = './output/01_raw_pdf_extract.txt'

# Define CVE list Output File
cve_output = './output/02_cve_extract.txt'

# Define Markdown Output File
md_output = './output/03_md_cve_list.txt'