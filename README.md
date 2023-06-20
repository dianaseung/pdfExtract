<h1 align="center">CVE-from-PDF Extract</h1>

<p align="center">
<img src="https://img.shields.io/maintenance/yes/2023?style=for-the-badge" alt="Maintenance" />
<img src="https://img.shields.io/github/last-commit/dianaseung/pdfExtract?style=for-the-badge" alt="Last Commit" />
<img src="https://img.shields.io/github/v/tag/dianaseung/pdfExtract?style=for-the-badge" alt="Latest Tag" />
<img src="https://img.shields.io/github/license/dianaseung/pdfExtract?style=for-the-badge" alt="License" />
</p>

---

## About CVE-from-PDF Extract: Overview
---
Python script to extract all CVE from a .pdf file into a .txt list, and format it into a JIRA-friendly or Excel/Google Sheets-friendly list, complete with hyperlink to NVD page.  

<p align="center"><img src="/media/pdfExtract-output.gif" alt="Preview of pdfExtract output" /></p>

*Note: Support for CVE and component extraction only; other mentions of security vulnerability such as SQL injection or XSS attacks must be manually extracted.*

---

### Functionality

What does this script do?
1. Extract text from a .PDF file to a .txt file (raw extract)
2. Input extract target: CVE, Component, or both
3. From .txt file (raw extract), find all extract target (i.e. CVE) into .txt file (CVE list)
4. Input format output: JIRA markdown format, or Excel sheet
4. From .txt file (CVE list), formats into JIRA-ready or Excel-ready list with hyperlinks, ready to copy and paste.


### Structure

<details>
<summary>Folder Structure</summary>
<br>

    pdfExtract
    ├── output/                                 # Directory of all output
    │   ├── 230620_151435                       # timestamp dir
    │   │   ├── 01_raw_pdf_extract.txt          # output file - Raw text extract from PDF
    │   │   ├── 02_cve_extract.txt              # output file - text list of CVE
    │   │   ├── 03_md_cve_list.txt              # output file - CVE list formatted
    ├── package                                 # 
    │   ├── setfiles.py                         # set output file names
    │   ├── get_raw.py                          # Step 1 - extract raw text from PDF
    │   ├── extract_cve.py                      # Step 2 - find all CVE in text
    │   ├── markdown_cve.py                     # Step 3 - format CVE list
    │   ├── ...                                 # 
    └ start.py                                  # Run script
    └ requirements.txt                          # Install dependencies
</details>


---

## Setup
Install [Python3](https://docs.python-guide.org/starting/install3/linux/) and [PIP](https://pip.pypa.io/en/stable/installation/) if not already installed 

### Installation / Setup
1. Install dependencies
    ```
    pip install -r requirements.txt
    ```
2. Place source PDF file in directory (i.e. `sample.pdf`)
    <p align="center"><img src="/media/pdfExtract-dir.png" alt="Example of pdfExtract dir with source PDF file" /></p>
3. Run script
    ```
    ./start.py
    ```
    - Input source PDF file name
    - Input extract target: CVE, component, or both
    - Input format output: JIRA or Excel
    <p align="center"><img src="/media/pdfExtract-script.gif" alt="Preview of running pdfExtract script" /></p>
4. See `/output/{timestamp}/` directory for output files
    - 01_raw_pdf_extract.txt
    - 02_cve_extract.txt
    - 03_md_cve_list.txt

---

## Upcoming Planned Features
- None yet