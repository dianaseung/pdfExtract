#!/usr/bin/env python3
# This reformats a txt list of CVEs into a Markdown-compatible list with NVD links

# Import required library.
import re
import os
from package.setfiles import cve_output as cve_output
from package.setfiles import md_output as md_output

def md_cve():
    format  = input("\n[ Format output ]: (JIRA or Excel) ")
    while format.lower() not in {"jira", "excel"}:
        format = input("\n[ Format output ]: (JIRA or Excel) ")

    # Open the file and create a pdf object.
    with open (cve_output, 'rt') as cve_list:
        x = 1
        y = 0
        for cve in cve_list:
            # Regex for checking if line is a CVE
            regex = r'CVE-\d{4,5}-\d{4,7}'
            regex_find = re.compile(regex)
            cleaned_cve = cve.strip().replace(' ', '')
            # If line matches CVE regex, convert it into an ordered list with CVE URL link.
            if regex_find.match(cve):
                if format.lower() == 'excel':
                    md_start = '=HYPERLINK("https://nvd.nist.gov/vuln/detail/'
                    md_url  = '", "'
                    md_end = '")'
                elif format.lower() == 'jira':
                    md_start = str(x) + '. ['
                    md_url  = '](https://nvd.nist.gov/vuln/detail/'
                    md_end = ')'
                else:
                    md_start = str(x) + '. ['
                    md_url  = '|https://nvd.nist.gov/vuln/detail/'
                    md_end = ']'
                print(md_start.strip(), cleaned_cve.strip(), md_url.strip(), cleaned_cve.strip(), md_end.strip(), sep="", file=open(md_output,'a'))
                x = x+1
            else:
                md_start = ' ' + str(y) + '.'
                md_end = '|'
                print(cleaned_cve.strip(), file=open(md_output, 'a'))
                y = y+1
    if (os.path.isfile(md_output) == True):
        print("SUCCESS: ", format, "formatting applied to CVE list from", cve_output, "to", md_output)

md_cve()