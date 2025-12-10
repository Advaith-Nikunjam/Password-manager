from interface import messagebox
from login import password_file
from packages import requests
from key import fer




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



#     --------------          Random Password Generator (API Integration)          ----------------

class password_creator:
    try:
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
    except:
        print("Network Down, can't generate password now!")




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