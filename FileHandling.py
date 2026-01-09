# text = "   I love Python    "
# print(text.strip())
users={}
def load_users():
    
    try:
        with open("data.txt","r")as file:
            for line in file:
                username,password=line.strip().split(",")
                users[username]=password
    except FileNotFoundError:
        print("no users found")
    return users

def save_users():

    with open ("users.txt","w")as file:
        for username,password in users.items():
            file.write(f"{username},{password}\n")

def login():
    username=input("enter username")
    password=input("enter password")
    if username in users and users[username]==password:
        print("login succesfully")
    else:
        print("error")

def register():
    username=input("choose username")
    password=input("choose password")

    if username in users:
        print("username already exist")
        return
    else:
        password = input("Choose password: ")
        users[username]=password
        save_users()
        print("Registration successful")

users = load_users()

while True:
    print("\n1. Login")
    print("2. Register")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        login()
    elif choice == "2":
        register()
    elif choice == "3":
        print("Bye 👋")
        break
    else:
        print("Invalid choice")
   