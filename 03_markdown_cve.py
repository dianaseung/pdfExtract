#!/usr/bin/env python3
# This reformats a txt list of CVEs into a Markdown-compatible list with NVD links  q

# Import required library.
import re
import os

# Open the file and create a pdf object.
#pdf = open("rawText.txt")

with open ('./output/cve_extract.txt', 'rt') as myfile:
    for eachLine in myfile:
        print('this is initial eachLine', eachLine)
        line = eachLine.strip().replace(' ', '')
        print('stripped line',line)
        md_start = '['
        md_url  = '|https://nvd.nist.gov/vuln/detail/'
        md_end = ']'
        print(md_start.strip(), line.strip(), md_url.strip(), line.strip(), md_end.strip(), sep="", file=open('./output/md_cve_list.txt','a'))

# with open ('./output/md_cve_list.txt', 'rt') as remove_space:
#     for line in remove_space:
#         print(line.replace(' ', '').strip(' \n'), file=open('./output/markdown_cve_list.txt', 'a'))

# os.remove("./output/md_cve_list.txt")