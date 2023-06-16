#!/usr/bin/env python3
# This extracts only the CVEs from a raw extracted PDF text

# Import required library.
import re
from package.setfiles import raw_output as raw_output
from package.setfiles import cve_output as cve_output

# Open the file and search text for regex match
def extract_cve():
    with open (raw_output, 'rt') as pdf_extract:
        for line in pdf_extract:
            regex = r'CVE-\d{4,5}-\d{4,7}'
            regex_find = re.compile(regex)
            result = regex_find.findall(line)
            if result:
                for x in result:
                    print(x, file=open(cve_output, 'a'))
    print("CVE list extracted from", raw_output, "to", cve_output)

extract_cve()