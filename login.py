from interface import ask_text,messagebox,root


#        --------  User  Login/Signup   ---------


while True:
    current_user = ask_text("Login","Enter username: ")

    master_pwd = ask_text("Password","Enter master password:",hidden=True)


    try:
        open("data/users.txt",'r').close()
    except:
        open("data/users.txt",'w').close()


    users = {}
    with open("data/users.txt","r") as f:
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
        with open("data/users.txt","a") as f:
            f.write(f"{current_user}:{master_pwd}\n")
            break
        

password_file = f"data/{current_user}_passwords.txt"