# CodeAlpha_EmailExtractor
# 📧 Email Extractor Using Python

A simple Python automation project that extracts email addresses from a text file and saves them into a separate file.

This project was developed as part of my **CodeAlpha Python Internship**.

## 🎯 Project Objective

The main objective of this project is to automate the process of finding email addresses in a text file and storing them in another file.

## ✨ Features

- Reads text from an input `.txt` file.
- Extracts email addresses using Regular Expressions.
- Removes duplicate email addresses.
- Displays the extracted email addresses in the terminal.
- Counts the total number of unique email addresses.
- Saves the results into a separate text file.

## 🛠️ Technologies Used

- **Python 3**
- `re` — Regular Expressions
- File Handling
- String Processing

## 📁 Project Structure

```text
CodeAlpha_EmailExtractor/
│
├── email_extractor.py
├── input.txt
├── extracted_emails.txt
└── README.md
```

## ⚙️ How It Works

1. The program reads the contents of `input.txt`.
2. A regular expression identifies email addresses.
3. Duplicate email addresses are removed.
4. The extracted addresses are displayed in the terminal.
5. The results are saved in `extracted_emails.txt`.

## ▶️ How to Run the Project

### Step 1: Install Python

Install Python 3 if it is not already installed.

### Step 2: Clone the Repository

```bash
git clone https://github.com/Arnab2762/CodeAlpha_EmailExtractor.git
```

### Step 3: Open the Project Folder

```bash
cd CodeAlpha_EmailExtractor
```

### Step 4: Run the Program

```bash
python email_extractor.py
```

Make sure `input.txt` is in the same folder as the Python script.

## 📝 Example Input

The `input.txt` file may contain:

```text
Hello,

Contact us at arnab@example.com.
For support, email support@company.com.
For internship queries, contact internship@codealpha.tech.

Thank you!
```

## 💻 Example Output

```text
===== EMAIL EXTRACTOR =====
Extracted email addresses:
arnab@example.com
support@company.com
internship@codealpha.tech

Total unique emails found: 3

Results saved to extracted_emails.txt
```

## 📚 Key Concepts Learned

- Python file handling
- Reading and writing text files
- Regular Expressions using the `re` module
- Lists and duplicate removal
- Loops and conditional statements
- Basic task automation

## 🎓 Internship

**Program:** Python Internship  
**Organization:** CodeAlpha  
**Task:** Task Automation with Python Scripts

## 👨‍💻 Author

**Arnab Sadhukhan**

GitHub: [Arnab2762](https://github.com/Arnab2762)

---

⭐ If you find this project useful, consider giving the repository a star!
