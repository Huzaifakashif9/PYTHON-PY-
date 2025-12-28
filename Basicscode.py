# name='huzaifa'
# print("my name is",name)


# count=0
# while count<=5:
#     print(count)
#     count+=1


# for i in range(1,6):
#     print(i)


# a=bool("false")
# print(type(a))


# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print()


# num1=float(input("enter a number"))
# num2=-float(input("enter a number"))
# print(num1*num2)


# name='ali'
# print(len(name))


# print(name.lower())


# x="hello"
# print(x[3])
# print(x[-1])

# p="programmingisfun"
# print(p[::-1])
# print(p[0:17:2])
# print(p[11:])
# print(p[15:10:-1])


# age=int(input("enter age"))
# if age>=18:
#     print("adult")
# else:
#     print("small")


# x=input("enter marks")
# if x>=90:
#     print("A")
# if x>=80:
#     print("B")
# if x>=70:
#     print("C")
# if x>=60:
#     print("D")
# if x<60:
#     print("Fail")


# age=int(input("enter age"))
# if age>=18:
#     nat=input("enter your nationality:").lower()
#     if nat=='pakistan':
#         print("you are pakistani")
#     else:
#         print("not a pakistani")
# else:
#     print("underage")


# name=["apple","mango","peach"]
# print(name[0])
# name[1]="rine"
# name.append("kiwi")
# name.insert(1,"melon")
# for i in name:
#     print(i)

# price=[10,20,30,40,50]
# for i in price:
#     if i>=30:
#         print(i,"is expensive")

# total=0
# for i in price:
#     total=total+i
#     average=total/len(price)
# print(total)


# for class_name in range(1,4):
#     print("class:",class_name)
#     for std_name in range(1,3):
#         print("student",std_name)


# n=input("enter number")
# for i in range(1,n+1):
#     print("table of",n)
#     for j in range(1,11):
#         print(n,"x",j,"=",n*j)


# for i in range(1,11):
#     if i%2==1:
#         print(i)

# h={'name':'huzaifa','age':18}
# print(h.get('name'))
# h['name']='karachi'
# h.pop('age')

# for k,v in h.items():
#     print(k,v)

# std={
#     "s1":{"name":"huzaifa","marks":18}
# }

# users=[
#     {
#         'name':"huzaiga","age":18
#     }
# ]
# for i in users:
#     print(i['name'])


# s={1,2,3,4,5,5,6,6}
# print(s)


# def greet(name):
#     print("hello",name)
# greet('huzaifa')

# def square(a):
#     total=a**2
#     return total
# result=square(5)
# print(result)

# def login(user,role="guest"):
#     print(user,role)
# login("ali")

# def total(*num):
#     print(num)
# total(1,2,3,4)

# def info(**j):
#     for k,v in j.items():
#         print(k,":",v)
# info(name='nonu',town='tbz')


# text=input("enter a number")
# mid=len(text)//2
# print(text[mid-2:mid+3])


# x=input("enter a string")
# upper=0
# lower=0
# digit=0
# for ch in x:
#     if ch.isupper():
#         upper+=1
#     if ch.islower():
#         lower+=1
#     if ch.isdigit():
#         digit+=1
# print("upper is",upper)
# print("lower is",lower)
# print("digit is",digit)



n=[1,2,3,-1,-2,4]
for i in n:
    if n[i]<0:
        n[i]=0
print(n)