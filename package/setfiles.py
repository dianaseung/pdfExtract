#!/usr/bin/env python3
import datetime
timestamp = datetime.datetime.now().strftime('%y%m%d_%H%M%S')

# Define raw PDF text Output File
raw_output = 'output/' + timestamp + '/01_raw_pdf_extract.txt'

# Define CVE list Output File
cve_output = 'output/' + timestamp + '/02_cve_extract.txt'

# Define Markdown Output File
md_output = 'output/' + timestamp + '/03_md_cve_list.txt'