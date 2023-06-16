#!/usr/bin/env python3
# This reformats a txt list of CVEs into a Markdown-compatible list with NVD links

# Import required library.
import re
import os
from package.setfiles import cve_output as cve_output
from package.setfiles import md_output as md_output

def md_cve():
    # Open the file and create a pdf object.
    with open (cve_output, 'rt') as cve_list:
        for cve in cve_list:
            cleaned_cve = cve.strip().replace(' ', '')
            md_start = '# ['
            md_url  = '|https://nvd.nist.gov/vuln/detail/'
            md_end = ']'
            print(md_start.strip(), cleaned_cve.strip(), md_url.strip(), cleaned_cve.strip(), md_end.strip(), sep="", file=open(md_output,'a'))
    print("Markdown format applied to CVE list from", cve_output, "to", md_output)

md_cve()