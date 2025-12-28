# print("my name is huzaifa")
# name="huzaifa"
# age=18
# print("my name is",name,"my age is",age)

# x=int(input("enter 1st number"))
# y=int(input("enter 2nd number"))

# print("sum",x+y)
# print("sub",x-y)
# print("mul",x*y)
# print('div',x/y)

# agge=int(input("enter your age"))
# if agge>=18:
#     print("adult")
# else:
#     print("junior")

# num=int(input("enter a number"))
# if num >0:
#     print("positive")
# elif num<0:
#     print("negative")
# else:
#     print("neutral")

# un=input("enter your name")
# pas=input("enter your password")
# if un=="huzaifa"and pas=="huz1234":
#     print("wlecome admin")
# else:
#     print("welcome user")

# a=int(input("enter 1st number"))
# b=int(input("enter 2nd number"))
# c=int(input("enter 3rd number"))
# # if a>=b and a>=c:
# #     print("a is greatest")
# # elif b>=a and b>=c:
# #     print("b is largest")
# # else:
# #     print('c is largest')
# #Option 2
# print("largest number is",max(a,b,c))

# for i in range(1,6):
#    print("huzaifa")

# fruits=["apple","mango","banana"]
# for fruit in fruits:
#     print(fruit)

# sum=0
# for i in range(1,6):
#     sum+=i
#     print(sum)

# i=1
# while i<=7:
#     print(i)
#     i+=1

# for i in range(1,11):
#     if i==2:
#         continue
#     print(i)
# for ini in range(10,0,-1):
#    print(ini)

# fruits=["apple","mango","banana"]
# print(fruits[0])
# fruits[1]="orange"
# print(fruits[1])
# fruits.append("grapes")
# print(fruits)
# fruits.insert(1,"pineapple")
# print(fruits)
# fruits.remove("pineapple")
# print(fruits)
# fruits.pop(1)
# print(fruits)

# a=[1,2,3,4,5,6]
# print(a[0:7:2])
# print(len(a))
# print(a.sort())
# print(a.reverse())
t=(1,2,3)
lst=list(t)
lst.append(4)
t=tuple(lst)
print(t)