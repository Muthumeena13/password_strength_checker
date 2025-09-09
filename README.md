# 🔐 Password Strength & Breach Checker

## ✅ Overview

This is a simple yet powerful **Password Strength & Breach Checker** tool built in Python, designed to run on **Google Colab**.  
It allows users to:
1. Check the strength of passwords based on common security rules.
2. Detect if a password has appeared in known data breaches using the [Have I Been Pwned API](https://haveibeenpwned.com/API/v3#PwnedPasswords).

---

## 🚀 Features

- ✅ Interactive: User inputs passwords directly.
- ✅ Password strength analysis:
    - Minimum length check (≥ 8 characters).
    - Uppercase letter presence.
    - Number inclusion.
    - Special character inclusion.
- ✅ Breach detection using k-anonymity method (efficient & secure).
- ✅ Parallel processing for fast multiple password checks.
- ✅ Displays progress with a progress bar.
- ✅ Presents final results in a clean tabular format.

---

## ⚡ How to Use

1. Open Google Colab: https://colab.research.google.com/
2. Copy & paste the code into a new notebook.
3. Run the notebook.
4. Enter the number of passwords you want to check.
5. Enter each password manually when prompted.
6. Wait for the analysis (progress bar will show).
7. View the final report in a nice table.

---

## ✅ Example Output

| Password       | Length >=8 | Has Uppercase | Has Number | Has Special Char | Times Breached |
|-------------- |------------|--------------|------------|-----------------|--------------|
| Admin@123     | True       | True         | True       | True            | 150          |
| letmein       | False      | False        | False      | False           | 50000        |
| S3cur3P@ssw0rd| True       | True         | True       | True            | 0           |

---

## ⚙️ Requirements

- Python 3.x  
- Google Colab (no extra installation needed)

### Python Libraries Used
- `re` (Regex)
- `hashlib`
- `requests`
- `pandas`
- `tqdm`
- `concurrent.futures`
- `IPython.display`

---

## ✅ Notes

- Breach check uses [Have I Been Pwned API](https://haveibeenpwned.com/API/v3#PwnedPasswords).
- Uses **SHA1 + k-anonymity** method to ensure security.
- Timeout and error handling included for network reliability.
- Threading is used to speed up multiple password checks.

---

## 🚧 Future Improvements (Optional)

- Add option to export results to CSV or PDF.
- Add graphical dashboard (e.g., using matplotlib).
- Support for batch input from file or GUI input.

---

## ⚡ License

MIT License – Free to use, modify, and distribute.

---

Made with ❤️ for learning and cybersecurity practice.
