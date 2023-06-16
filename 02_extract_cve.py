#!/usr/bin/env python3
# This extracts only the CVEs from a raw extracted PDF text

# Import required library.
import re

# Define Input File
raw_output = './output/raw_pdf_extract.txt'

# Define Output File
cve_output = './output/cve_extract.txt'

# Open the file and search text for regex match
with open (raw_output, 'rt') as pdf_extract:
    for line in pdf_extract:
        regex = r'CVE-\d{4,5}-\d{4,7}'
        regex_find = re.compile(regex)
        result = regex_find.findall(line)
        if result:
            for x in result:
                print(x, file=open(cve_output, 'a'))