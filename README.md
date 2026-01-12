# 🔐 Password Manager Application

## 📌 Project Overview
This project is a simple **Password Manager Application** built using **Python**.  
It allows users to securely store, view, and search passwords using **encryption**, **Object-Oriented Programming (OOP)** principles, and a **Linear Search algorithm**.

The application uses a dialog-based **GUI (Tkinter)** and encrypts all stored passwords to ensure security.

---

## 🎯 Features
- User login and signup system
- Secure password storage using encryption (Fernet)
- View saved passwords
- Search for a specific account password
- Automatic password generation using an external API
- Simple and user-friendly GUI

---

## 🧠 Concepts Used
- **Object-Oriented Programming (OOP)**
  - Classes and objects
  - Inheritance
  - Encapsulation
- **Algorithm Design**
  - Linear Search for finding stored passwords
- **Security**
  - Symmetric encryption using Fernet
- **File Handling**
  - Storing user data and encrypted passwords in files
- **GUI Development**
  - Tkinter dialogs for user interaction

---

## 🏗️ Project Structure
project/
├── main.py
├── login.py
├── password.py
├── key.py
├── interface.py
├── packages.py
├── README.md
├── requirements.txt
└── data/



---

## 🔍 Algorithm Used
### Linear Search
- Searches passwords by checking entries one by one
- Stops immediately when a match is found
- Chosen for simplicity and suitability for small datasets

---

## 🔐 Security Implementation
- Passwords are encrypted before being stored
- Encryption uses **Fernet symmetric encryption**
- Passwords are decrypted only when needed

---

## ▶️ How to Run the Project
1. Make sure Python is installed
2. Install required libraries:
pip install cryptography requests



3. Run the main file:
python main.py


---

## 🚀 Future Improvements
- Use a database instead of text files
- Hash master passwords instead of storing them directly
- Improve GUI with a full window interface
- Add password strength validation

---

## 📚 Learning Outcomes
- Practical use of OOP concepts
- Understanding algorithm design in real applications
- Implementing encryption for data security
- Combining GUI, algorithms, and file handling in one project