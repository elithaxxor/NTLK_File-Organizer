# NLTK Cyber Security Auditor & Organizer 📁🔍

This repository includes Python scripts designed to assist in auditing and organizing cybersecurity-related documents and resources using Python and the Natural Language Toolkit (NLTK).

---
## 🚀 **Scripts Included**
- **[`cyber-secururity-auditor.py`](https://github.com/elithaxxor/NTLK_File-Organizer/blob/main_pi/NLTK_File-Organizer/cyber-secururity-auditor.py)** — Audits cybersecurity documents and content for compliance and best practices.
- **[`cyber-security-organizer.py`](https://github.com/elithaxxor/NTLK_File-Organizer/blob/main_pi/NLTK_File-Organizer/cyber-security-organizer.py)** — Organizes cybersecurity resources and documents systematically using NLP techniques.
- **[`cyber-security-organizer.py`](https://github.com/elithaxxor/NTLK_File-Organizer/blob/main_pi/NLTK_File-Organizer/cyber-security-auditor.py)** — Organizes cybersecurity resources and documents systematically using NLP techniques.

---
## 🛠️ **Features**

### **Cyber Security Auditor**
- Performs detailed analysis of cybersecurity-related documents.
- Identifies compliance-related items and potential areas for improvements.
- Generates a concise summary/report of audit results.
- Uses NLTK for deeper text analysis and insights.

### **Cyber Security Organizer**
- Automatically categorizes and organizes various cybersecurity files and documents.
- Leverages Natural Language Processing to intelligently group related files.
- Simplifies managing a large volume of cybersecurity documentation.

---
## 📥 **Installation**

Clone the repository:
```bash
git clone https://github.com/elithaxxor/NTLK_File-Organizer.git
cd NLTK_File-Organizer
```

```markdown
# NLTK Cyber Security Auditor & Organizer 📁🔍

This repository includes Python scripts designed to assist in auditing and organizing cybersecurity-related documents and resources using Python and the Natural Language Toolkit (NLTK).

---
## 🚀 **Scripts Included**
- **[`cyber-secururity-auditor.py`](https://github.com/elithaxxor/NTLK_File-Organizer/blob/main_pi/NLTK_File-Organizer/cyber-secururity-auditor.py)** — Audits cybersecurity documents and content for compliance and best practices.
- **[`cyber-security-organizer.py`](https://github.com/elithaxxor/NTLK_File-Organizer/blob/main_pi/NLTK_File-Organizer/cyber-security-organizer.py)** — Organizes cybersecurity resources and documents systematically using NLP techniques.

---
## 🛠️ **Features**

### **Cyber Security Auditor**
- Performs detailed analysis of cybersecurity-related documents.
- Identifies compliance-related items and potential areas for improvements.
- Generates a concise summary/report of audit results.
- Uses NLTK for deeper text analysis and insights.

### **Cyber Security Organizer**
- Automatically categorizes and organizes various cybersecurity files and documents.
- Leverages Natural Language Processing to intelligently group related files.
- Simplifies managing a large volume of cybersecurity documentation.

---
## 📥 **Installation**

Clone the repository:
```bash
git clone https://github.com/elithaxxor/NTLK_File-Organizer.git
cd NLTK_File-Organizer
```

Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate    # On Windows use `venv\Scripts\activate`
```

Install required packages:
```bash
pip install -r requirements.txt
```


⚠️ **Note:** Ensure you have Python installed ([Python download](https://www.python.org/downloads/)).

---
## 📖 **Usage**

### **Cyber Security Auditor**
Run the audit script with:
```bash
python cyber-secururity-auditor.py
```

### **Cyber Security Organizer**
Run the organizer script with:
```bash
python cyber-security-organizer.py
```

You can modify the scripts according to your directory structure or specific use-cases.

---
## 💻 **Tech Stack**

- [Python](https://www.python.org/)
- [NLTK (Natural Language Toolkit)](https://www.nltk.org/)

---
```markdown
# NLTK File Organizer

## Overview

This document describes the updates and features added to the `CybersecurityFileCategorizer` class, which utilizes the NLTK library for organizing your cybersecurity tools.

## Features

### 1. Magic Library
- **Import**: `import magic` is added for file type detection.
- **Installation**: 
  ```bash
  pip install python-magic  # For Linux/MacOS
  pip install python-magic-bin  # For Windows
  ```

### 2. `_extract_metadata` Method
- **Purpose**: Extracts metadata from a given file.
- **Logic**:
  - Uses `magic.from_file(filepath)` to get the file type.
  - Uses `os.path.getsize(filepath)` to get the file size.
  - Uses `os.path.getctime(filepath)` and `os.path.getmtime(filepath)` to get the creation and modification times, respectively.
  - Formats the timestamps using `datetime.fromtimestamp().strftime()`.
  - Returns a dictionary containing the extracted metadata.
  - Includes error handling in case metadata extraction fails.

### 3. `analyze_files` Method
- **Purpose**: Analyzes files in the input directory, extracts metadata, and generates a report.
- **Logic**:
  - Creates an empty dictionary `analysis_results` to store the results.
  - Calls `self.categorize_files()` to get the categorization results.
  - Iterates through the files in the input directory.
  - For each file, calls `self._extract_metadata()` to get the metadata.
  - Stores the metadata and the category (from categorization results) in the `analysis_results` dictionary.
  - Returns the `analysis_results` dictionary.

### 4. `generate_analysis_report` Method
- **Purpose**: Generates a report of the file analysis and saves it to a JSON file.
- **Logic**:
  - Takes the `analysis_results` dictionary as input.
  - Uses `json.dump()` to save the results to a JSON file (default name: `analysis_report.json`).
  - Includes error handling in case report generation fails.

### 5. `main` Function Refactoring
- **Menu System**:
  - Presents a menu with options: "Categorize Files," "Analyze Files," and "Exit."
  - Uses a `while` loop to keep the menu running until the user chooses to exit.
  - Uses `input()` to get the user's choice.
- **Choice Handling**:
  - **Choice 1 (Categorize Files)**:
    - Calls `categorizer.categorize_files()`.
    - Prints the results.
    - Saves the results to CSV and PDF.
    - Asks the user if they want to copy or move the files.
  - **Choice 2 (Analyze Files)**:
    - Calls `categorizer.analyze_files()`.
    - Prints the analysis results, including metadata and category.
    - Calls `categorizer.generate_analysis_report()` to save the report to a JSON file.
  - **Choice 3 (Exit)**:
    - Breaks out of the `while` loop, ending the program.
  - **Invalid Choice**:
    - Prints an error message if the user enters an invalid choice.

### 6. File Metadata Storage
- The `CybersecurityFileCategorizer` class now has a `self.file_metadata` dictionary to store the extracted metadata.

### 7. Import `json`
- Added `import json` to the top of the file.

## How to Run the Updated Code

1. Ensure all required libraries are installed:
   ```bash
   pip install python-magic
   pip install json
   ```

2. Run the script:
   ```bash
   python categorize.py
   ```

3. Follow the on-screen prompts to categorize or analyze your files.

---

This document provides a detailed overview of the new features and updates to the `CybersecurityFileCategorizer` class to help you better organize your cybersecurity tools.
```

Feel free to adjust the content as necessary to better fit your needs or any additional features you may want to highlight.
