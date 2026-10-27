common_passwords = ["123456", "password", "qwerty", "admin"]
password = input("Create a password: ")

for i in common_passwords:
    if password == i:
        print("Password too common!")
        break
else:
    print("Password accepted!")

