# 🔐 Password Strength Checker + Breach Check

This is a beginner-friendly cybersecurity project that evaluates password strength and checks whether the password has appeared in known data breaches using the HaveIBeenPwned API.

## ✅ Features
- Password strength evaluation (based on length, character types)
- Entropy calculation
- Breach check via HaveIBeenPwned API (k-anonymity method)
- Suggestions to improve password quality

## 📁 Project Structure
```
password_checker/
├── password_checker.py       # Main logic
├── utils.py                  # Helper functions
├── requirements.txt          # Required libraries
├── README.md                 # Project documentation
```

## 📦 Installation
```bash
pip install -r requirements.txt
```

## 🚀 How to Run
```bash
python password_checker.py
```

## 📌 Sample Output
```
🔐 Password Strength Checker + Breach Check 🔐

Enter your password: Hello@123

Password Strength: Strong
Entropy Score: 68.16 bits
✅ This password has NOT been found in known breaches.

Suggestions to Improve:
- Use at least 12 characters.
```

## 🧠 Concepts Covered
- Cryptographic hashing (SHA1)
- K-Anonymity
- Password entropy
- Secure API usage

## 🛠 Future Improvements
- Add a GUI (e.g., with Streamlit)
- Include a password generator
- Export report logs to file

## 🧪 Reference
- https://haveibeenpwned.com/API/v3
