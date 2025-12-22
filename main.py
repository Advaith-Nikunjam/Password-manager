from interface import ask_text,root,messagebox
from password import random_pass
from password import PasswordSearch
from login import password_file
from key import fer



#     -----------    Main Code - Where user inputs his choice    ---------


manager = PasswordSearch(password_file,fer)
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