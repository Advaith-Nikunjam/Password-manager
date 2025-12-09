from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import simpledialog,messagebox


root = tk.Tk()
root.withdraw()

def ask_text(title,prompt,hidden=False):
    while True:
        if hidden:
            value = simpledialog.askstring(title,prompt,show='*')
        else:
            value = simpledialog.askstring(title,prompt)
        
        if value is None:
            if messagebox.askyesno("Quit","Do you want to quit:"):
                root.destroy()
                quit()
            else:
                continue
        value = value.strip()

        if value == "":
            messagebox.showerror("Error","Please enter a value.")
            continue
        return value


def load_key():
    file = open('key.key','rb')
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)


while True:
    current_user = ask_text("Login","Enter username: ")

    master_pwd = ask_text("Password","Enter master password:",hidden=True)


    try:
        open("users.txt",'r').close()
    except:
        open("users.txt",'w').close()


    users = {}
    with open("users.txt","r") as f:
        for line in f:
            u,p = line.strip().split(":")
            users[u] = p

    if current_user in users:
        if users[current_user] != master_pwd:

            retry = messagebox.askyesno("Wrong Password","Wrong Password, do you want to try again?")
            if retry:
                continue
            else:
                messagebox.showinfo("Exit","Thank you!")
                root.destroy()
                quit()

        messagebox.showinfo("Login","Login Successful")
        break
    else:
        messagebox.showinfo("Newuser","New user created")
        with open("users.txt","a") as f:
            f.write(f"{current_user}:{master_pwd}\n")
            break
        

password_file = f"{current_user}_passwords.txt"



def add():
    name = ask_text("Account","Account name: ")
    pwd = ask_text("Password","Password: ")


    with open(password_file,'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

    messagebox.showinfo("Saved","Password Saved.")

def view():
    try:
        with open(password_file,'r') as f:
            line = f.readlines()
            if not line:
                messagebox.showinfo("view password.","No saved Password.")
                return
            
            out = []

            for lines in line:
                data = lines.rstrip()
                if "|" not in data:
                    continue
                user,passw = data.split("|",1)
                out.append(f"User name:{user} , Password:{fer.decrypt(passw.encode()).decode()}")
            messagebox.showinfo("Saved Passwords","\n".join(out))
    except FileNotFoundError:
        messagebox.showinfo("View Passwords","No saved passwords")


while True:
    choice = ask_text(
        "Menu",
        "Do you want to add a password, view existing ones or do you want to quit: ").lower()


    if choice == "q" or choice == "quit":
        break

    elif choice == "add":
        add()

    elif choice == "view":
        view()

    else:
        messagebox.showerror("Invalid Choice","Its an invalid choice, Make a valid one")
        
root.destroy()
