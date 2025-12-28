user_id= input("enter your id")
user_pass=input("enter your password")
age=int(input("enter your age"))
id_ok=len(user_id)>=5
pass_ok=len(user_pass)>=8
age_ok=age>=18
if id_ok and pass_ok and age_ok:
    print("login successful")
else:
    print("error")

if not id_ok:
    print("id should contain atleast 5 characters")
if not pass_ok:
    print("password should contain atleast 8 characters")
if not age_ok:
    print("age should be atleast 18")

uname=input("name??")
upass=input("password")
if uname=="admin" and upass=="1234":
    print("login successful")
elif uname=="admin" and upass!="1234":
    print("wrong password")
elif uname!="admin":
    print("user not found")
else:
    print("nothing")

user_type = input("Enter user type (premium/regular/guest): ").lower()
bill_amount = float(input("Enter total bill amount: "))

if user_type == "premium" :
    discount = 0.20
elif user_type == "regular":
    discount = 0.10
else:
    discount = 0.0
final_price = bill_amount * (1 - discount)

print("user type:",user_type)
print("bill amount:",bill_amount)
print("total disocunt:",discount*100)
print("amount after disocunt:",final_price)

print("\n\n")

salary = float(input("Enter monthly salary : "))
credit_score = int(input("Enter credit score: "))
if salary > 50000 and credit_score > 700:
    print("Loan Approved")
elif salary > 30000 and credit_score > 650:
    print("Further Verification Required")
else:
    print("Loan Rejected")