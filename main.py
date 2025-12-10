from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import simpledialog,messagebox
import requests

#   ------     Making the GUI     -------


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



#     ------- creating or using fernet key  --------


while True:
    try:
        def load_key():
            file = open('key.key','rb')
            key = file.read()
            file.close()
            return key

        key = load_key()
        fer = Fernet(key)
        break

    except:
        def writing_key():
            key = Fernet.generate_key()
            with open('key.key','wb') as key_file:
                key_file.write(key)

        writing_key()
        continue



#        --------  User  Login/Signup   ---------


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
            line = line.strip()
            if ":" not in line:
                continue
            u,p = line.split(":")
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


#  ----------  storing user password in specific files   ------------


class password_manager:


    def __init__(self,password_file,fer):
        self.password_file = password_file
        self.fer = fer

    def add(self,name,pwd):
        #name = ask_text("Account","Account name: ")
        #pwd = ask_text("Password","Password: ")


        with open(self.password_file,'a') as f:
            f.write(name + "|" + self.fer.encrypt(pwd.encode()).decode() + "\n")

        messagebox.showinfo("Saved","Password Saved.")

    def view(self):
        try:
            with open(self.password_file,'r') as f:
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
                    out.append(f"User name:{user} , Password:{self.fer.decrypt(passw.encode()).decode()}")
                messagebox.showinfo("Saved Passwords","\n".join(out))
        except FileNotFoundError:
            messagebox.showinfo("View Passwords","No saved passwords")





class password_creator:
    def __init__(self):
        self.base_url = f"https://api.genratr.com/?length=8&uppercase&lowercase&special&numbers"
    def generate_password(self):
        
        url = self.base_url
        responce = requests.get(url)

        if responce.status_code == 200:
            return responce.text.strip()
        else:
            print(f"Data retrievel failed, Error code: {responce}")
            return None




random_pass = password_creator()


#   ------------    Search algorithm       -----------


class Search_option(password_manager):
    def search(self,target):
        try:
            with open(self.password_file,'r') as f:
                for line in f:
                    data = line.rstrip()

                    if "|" not in data:
                        continue
                    user,passw = data.split("|",1)
                    if user.lower() == target.lower():
                        plain = self.fer.decrypt(passw.encode()).decode()
                        return plain
                
            return None
        except FileNotFoundError:
            return None




manager = Search_option(password_file,fer)


#     -----------    Main Lopp - Where user inputs his choice    ---------



while True:
    choice = ask_text(
        "Menu",
        "Do you want to add a password, view existing ones, search a specific account or do you want to quit: ").lower()


    if choice == "q" or choice == "quit":
        break

    elif choice == "add":
        name = ask_text("Account Name","Account Name: ")
        # pwd = ask_text("Password","Password: ")

        auto_pass = messagebox.askyesno(
            "Password option",
            "Do you want to auto generate password? "
        )

        if auto_pass:
            pwd = random_pass.generate_password()
            if pwd is None:
                messagebox.showerror("Error","Could not generate password. create manually")
                pwd = ask_text("Password","Password: ")
            
            else:
                messagebox.showinfo("Generated Password",f"Generated Password:\n {pwd}")

        else:
            pwd = ask_text("Password","Password: ")

        manager.add(name,pwd)

    elif choice == "view":
        manager.view()

    elif choice == "search":
        target = ask_text("Account Name:","Enter Account Name You want to search: ")
        result = manager.search(target)
        if result is None:
            messagebox.showinfo("Search result",f"No Account Name named {target}")
        else:
            messagebox.showinfo("Search result",f"Password for {target}:{result}")

    else:
        messagebox.showerror("Invalid Choice","Its an invalid choice, Make a valid one")
        
root.destroy()