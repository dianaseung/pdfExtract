#!/usr/bin/env python3
# This extracts only the CVEs from a raw extracted PDF text

# Import required library.
import re
import os
from package.setfiles import raw_output as raw_output
from package.setfiles import cve_output as cve_output

# Open the file and search text for regex match
def extract_cve():
    with open (raw_output, 'rt') as pdf_extract:
        # Arrays for checking for Duplicates
        raw_list = []
        dup_list = []
        extract_target  = input("\n[ Extract target ]: (cve, keyword or both) ")
        while extract_target.lower() not in {"cve", "keyword", "both"}:
            extract_target = input("\n[ Extract target ]: (cve, keyword or both) ")

        keyword = input("[ Input keyword to search: ] ")
        # Check the raw PDF extract line by line for regex match
        for line in pdf_extract:
            # This regex searchs for either CVE or Component mentions -- adjust regex here as needed
            if extract_target.lower() == 'cve':
                regex = r'CVE-\d{4,5}-\d{4,7}'
            elif extract_target.lower() == 'keyword':
                regex = re.escape(keyword) + r'+(\S+)'
            elif extract_target.lower() == 'both':
                regex = r'(CVE-\d{4,5}-\d{4,7}|' + re.escape(keyword) + r'+(\S+))'
            else:
                regex = r'CVE-\d{4,5}-\d{4,7}'
            regex_find = re.compile(regex)
            result = regex_find.findall(line)   
            # If result is not empty
            if result:
                for x in result:
                    # To print all including duplicates
                    if extract_target == 'cve':
                        if x not in raw_list:
                            raw_list.append(x)
                        else:
                            dup_list.append(x)
                    elif extract_target == 'keyword':
                        # Since findall can return multiple results, just check first result and append it if it doesn't exist
                        if x not in raw_list:
                            raw_list.append(x)
                        else:
                            dup_list.append(x)
                    elif extract_target == 'both':
                        if x[0] not in raw_list:
                            raw_list.append(x[0])
                        else:
                            dup_list.append(x[0])
                    else:
                        if x[0] not in raw_list:
                            raw_list.append(x[0])
                        else:
                            dup_list.append(x[0])
        # Print all uniques in raw_list to cve_output file
        for i in range(len(raw_list)):
            print(raw_list[i], file=open(cve_output, 'a'))
    if (os.path.isfile(cve_output) == True): 
        print("SUCCESS: CVE list extracted from", raw_output, "to", cve_output)

extract_cve()
