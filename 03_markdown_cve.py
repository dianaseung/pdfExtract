#!/usr/bin/env python3
# This reformats a txt list of CVEs into a Markdown-compatible list with NVD links

# Import required library.
import re
import os

# Open the file and create a pdf object.
cve_output = './output/cve_extract.txt'
with open (cve_output, 'rt') as cve_list:
    for cve in cve_list:
        cleaned_cve = cve.strip().replace(' ', '')
        md_start = '['
        md_url  = '|https://nvd.nist.gov/vuln/detail/'
        md_end = ']'
        print(md_start.strip(), cleaned_cve.strip(), md_url.strip(), cleaned_cve.strip(), md_end.strip(), sep="", file=open('./output/md_cve_list.txt','a'))