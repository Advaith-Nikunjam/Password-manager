from packages import Fernet

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
