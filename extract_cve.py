#!/usr/bin/env python3

# Import required library.
import re

# Open the file and create a pdf object.
#pdf = open("rawText.txt")

with open ('./output/raw_pdf_extract.txt', 'rt') as myfile:
    for eachLine in myfile:
        caseMatch = r'CVE-\d{4,5}-\d{4,7}'
        regex_find = re.compile(caseMatch)
        result = regex_find.findall(eachLine)
        if result:
            for x in result:
                print(x, file=open('./output/cve_extract.txt', 'a'))