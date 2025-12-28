students=["ali","huzaifa","ahmed","sher"]
for i in students:
    print(i)

numbers=[10,20,30,40,50]
for multiple in numbers:
    print(multiple*2)

marks=[85,38,100,75,22,56]
for m in marks:
    if m>50:
        print("pass")
    else:
        print("fail")

pricee=[1200,500,1500]
for price in pricee:
    if price>1000:
        print(price,"is expensive")

temp=[30,35,20,25]
for t in temp:
    if t>25:
        print(t,"is the temperature")
    
a='python'
for i in a:
    print(i)

for i in range(0,6):
    print(i)

for hey in range(0,8,2):
    print(hey)

hey=[10,20,30,40,50,60,70,80]
total=0
for i in hey:
    total=total+i
print(total)

marks=[10,30,20,40]
total=0
for i in marks:
    total=total+i
average=total/len(marks)
print(average)

#nested for start
for class_name in range(1,4):
    print("class:",class_name)
    for student_name in range(1,5):
        print("        student",student_name)

for team in range(1,4):
    for std in range(1,6):
        print("team",team,"member",std)

n=int(input("enter any number"))
for n in range(1,n+1):
    for k in range(1,11):
        print(n,"x",k,"=",n*k)

for i in range(5,51,5):
    print(i)

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
for i in range(start+1, end + 1):
    print(i)

for i in range(1,11):
    print("number:",i**2,i**3)

for i in range(1,6):
    print("#"*i)

for i in range(5,0,-1):
    print("#"*i)