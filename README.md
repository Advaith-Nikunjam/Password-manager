🔐 Python Password Manager (CLI)

A simple command-line password manager built in Python using Fernet encryption from the cryptography library.
Each user has their own username + master password and a separate encrypted password storage file.

✨ Features

Create account (username + master password)

Login using your own credentials

Save passwords securely (encrypted)

View saved passwords (decrypted when showing)

Separate file for each user

Fernet encrypted storage

Minimal & beginner-friendly

🧠 How it works

Fernet key is generated once using cryptography

All saved passwords are encrypted using this key

Your credentials are stored in users.txt

The program loads your personal vault file:

<username>_passwords.txt

🗂 File structure
.
├── users.txt                 # usernames + master passwords
├── key.key                   # Fernet encryption key
├── <username>_passwords.txt  # encrypted user passwords
└── main.py                   # main program

▶️ Usage
1. Install required lib
pip install cryptography

2. Run the program
python main.py

3. Choose option
add   → add new password
view  → view saved passwords
quit  → exit

🔑 Example
Enter username: john
Enter master password: abcd1234

New user created!

add / view / quit: add
User name: gmail
Password: myPassword123

🛠 Built using

Python

cryptography.Fernet

basic file handling

🔒 Security note

This is intended for learning purposes only.
Possible future improvements:

hash master passwords

separate encryption key per user

hidden password input (using getpass)

better UI / GUI

📌 Goal

This project was made to learn:

encryption basics

storing credentials securely

building CLI tools

user authentication

📍 Future Ideas

update / delete stored passwords

copy to clipboard

convert to Tkinter GUI

online sync / backup

hashed master passwords