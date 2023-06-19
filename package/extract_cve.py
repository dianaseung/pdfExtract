#!/usr/bin/env python3
# This extracts only the CVEs from a raw extracted PDF text

# Import required library.
import re
from package.setfiles import raw_output as raw_output
from package.setfiles import cve_output as cve_output

# Open the file and search text for regex match
def extract_cve():
    with open (raw_output, 'rt') as pdf_extract:
        # Arrays for checking for Duplicates
        raw_list = []
        dup_list = []
        # Check the raw PDF extract line by line for regex match
        for line in pdf_extract:
            # This regex searchs for either CVE or Component mentions -- adjust regex here as needed
            regex = r'(CVE-\d{4,5}-\d{4,7}|Components+(\S+))'
            regex_find = re.compile(regex)
            result = regex_find.findall(line)
            # If result is not empty
            if result:
                for x in result:
                    # Since findall can return multiple results, just check first result and append it if it doesn't exist
                    if x[0] not in raw_list:
                        raw_list.append(x[0])
                    else:
                        dup_list.append(x[0])
        # Print all uniques in raw_list to cve_output file
        for i in range(len(raw_list)):
            print(raw_list[i], file=open(cve_output, 'a'))
                    
    print("CVE list extracted from", raw_output, "to", cve_output)

extract_cve()