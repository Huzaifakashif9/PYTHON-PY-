hello=[i for i in range(1,11) if i %2==1]
print(hello)

h=[i for i in range(1,26) if i%5==0]
print(h)

nums = [1, 2, 3, 4, 5, 6]
rev=[]
print(nums[::-1])
nums.reverse()
print(nums)


nums = [1, 2, 3, 5, 6]
for i in range(1,7):
    if i not in nums:
        print("missing is",i)


num = int(input("Enter number: "))
is_prime = True
if num<2:
    is_prime=False
else:
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break
if is_prime:
    print("Prime number")
else:
    print("Not prime")
            

nums = [1, 2, 2, 3, 4, 3, 5]
p=[]
for i in nums:
    if i not in p:
        p.append(i)
print(p)


word = "madam"
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


users = {
    "admin": "1234",
    "huzaifa":"abcd"
}

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username] == password:
        print(" Login Successful")
    else:
        print(" Invalid Username or Password")


def register():
    username = input("Choose username: ")

    if username in users:
        print(" Username already exists")
        return

    password = input("Choose password: ")
    users[username] = password
    print(" Registration successful")


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
        print("Bye ")
        break
    else:
        print("Invalid choice")
