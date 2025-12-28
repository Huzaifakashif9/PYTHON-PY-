def greet(name):
    print("hello",name)
greet('huzaifa')

def square(a):
    total=a*a
    return total
result=square(7)
print(result)

def login(user,role="guest"):
    print("user",user)
    print("role",role)
login('huzaifa')

def add(a,b):
    print(a+b)
add(3,5)

def multiply(a,b):
    return a*b
result=multiply(5,5)
print(result)

def calc(a,b):
    return a+b,a*b,a-b
d,f,g=calc(10,2)
print(d,f)

# agar input ki exact quamntity na pata ho so use ARGS
def total(*numbers):
    print(sum(numbers))
total(1,2,3,4)

def phal(*fruits):
    for f in fruits:
        print("phal hai:",f)
phal('aam','seb','kela')

# key value me data dl sara dictionary banke output ata hai so it is KWARGS

def std(**info):
    print(info)

std(name="nonu",age=18)

def showdata(**data):
    for k,v in data.items():
        print(k,":",v)
showdata(name="ali",age=19)

# kwargs + normal args
def company(names,**subname):
    print('item',names)
    print("description",subname)
company('laptop',name='dell',price=125)

# args with kwars
def iphone(a,b,*i,**ip):
    print("a is:",a)
    print("b is:",b)
    print("c is:",i)
    print("d=",ip)
iphone(1,2,3,4,5,name="ali")

balance = 1000

def check_balance():
    print('Your balance is:', balance)

def deposit(amount):
    global balance
    balance = balance + amount
    print(amount, 'added successfully')
    print("Total balance after deposit:", balance)

def withdrawal(amount):
    global balance
    if amount > balance:
        print('Insufficient balance')
    else:
        balance = balance - amount
        print(amount, 'withdrawn successfully')
        print("Remaining balance is:", balance)

while True:
    print("\n--- HBL ATM Menu ---")
    print("1. Check your balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        check_balance()      
    elif choice == 2:
        a = int(input("Enter amount you want to deposit: "))
        deposit(a)
    elif choice == 3:
        b = int(input("Enter amount you want to withdraw: "))
        withdrawal(b)
    elif choice == 4:
        print("Thank you for using HBL ATM!")
        break
    else:
        print("Invalid choice")
