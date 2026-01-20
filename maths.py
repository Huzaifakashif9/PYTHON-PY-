#to reverse a number
a=int(input("enter a number"))
b=int(input("enter a number"))
a=a+b
b=a-b
a=a-b
print("now a is",a)
print(f"now b is {b}")


#fabonacchi series
num=int(input("enter a number"))
a=0
b=1
for i in range(1,num):
    print(a)
    c=a+b
    a=b
    b=c


#duplicate check
lst=[1,2,3,1,2,4,3,5,6,5,7]
unique=[]
for i in lst:
    if i not in unique:
        unique.append(i)
print("after rmoving duplciate",unique)


#vowel check
non=input("enter a word")
count=0
for ch in non:
    if ch in "aeiou":
        count+=1
print("total vowels are",count)



#prime num check
num=int(input("enter a number"))
for i in range(2,num):
    if num>0:
        if num%i==0:
            print("not a prime")
            break
        else:
            print('prime number hai')
            break
    else:
        print("galat number h")


#finding greatest

a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))

if a<0 or b<0 or c<0:
    print("value smaller than 0 cant be proceeded")
elif a==b==c:
    print("all cant be same to find greatest")
elif a>b and a>c:
    print("a is greatest")
elif b>a and b>c:
    print("b is greatest")
else:
    print("c is greatest")



#reverse a string
s = "i love python"
print(s[::-1])


#reverse string not words
s = "i love python"
print(" ".join(s.split()[::-1]))


#remove duplicate
nums = [1, 2, 3, 2, 4, 1, 5]
print(list(set(nums)))



#reverse string without slicing
def reverse(s):
    p=''
    for ch in s:
        p=ch+p
    return p
print(reverse("ali"))


# Password Strength Checker
password=input("enter a password")

has_upper=False
has_digit=True

for i in password:
    if i.isupper():
        has_upper=True
    if i.isdigit():
        has_upper=True

if len(password)>=10 and has_upper and has_digit:
    print("strong passwords")
elif len(password)>=6 and has_upper or has_digit:
    print("medium password")
else:
    print("weak password")