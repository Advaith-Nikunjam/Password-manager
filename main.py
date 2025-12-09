from cryptography.fernet import Fernet

'''
def writing_key():
    key = Fernet.generate_key()
    with open('key.key','wb') as key_file:
        key_file.write(key)

writing_key()
'''
def load_key():
    file = open('key.key','rb')
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

current_user = input("Enter username: ")

master_pwd = input("Enter master password:")


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
        print("wrong Password")
        quit()
    print("Login Successful")
else:
    print("New user created")
    with open("users.txt","a") as f:
        f.write(f"{current_user}:{master_pwd}\n")
    

password_file = f"{current_user}_passwords.txt"



def add():
    name = input("User name: ")
    pwd = input("Password: ")

#fer.encrypt(pwd.encode()).decode()
#fer.decrypt(passw.encode()).decode()
    with open(password_file,'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

def view():
    try:
        with open(password_file,'r') as f:
            for lines in f.readlines():
                data = lines.rstrip()
                user,passw = data.split("|")
                print("User name:",user,",Password",fer.decrypt(passw.encode()).decode())
    except:
        print("No saved passwords")


while True:
    choice = input("Do you want to add a password or view existing ones, or do you want to quit(q): ").lower()


    if choice == "q" or choice == "quit":
        break

    elif choice == "add":
        add()

    elif choice == "view":
        view()

    else:
        print("Its an invalid choice")
        print("Make a valid one")
        continue
