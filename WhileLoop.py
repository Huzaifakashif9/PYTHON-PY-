total=0
ask=int(input("enter any number"))
while ask!=0:
    total = total+ask
    ask=int(input("enter any number"))
print(total)

i=0
while i<5:
    print(i)
    i=i+1

num=int(input("enter any number"))
while num>0:
    print(num)
    num=num-1

password=input("enter a password")
while password!="python123":
    password=input("enter a password")
print("accessed")

num = int(input("Enter a number between 1 - 10"))
while num < 1 or num > 10:
  num = int(input('Invalid Entry, try again: '))
print('Thanks, you have entered',num)