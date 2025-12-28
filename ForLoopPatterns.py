names=["ali","huzaifa","hani"]
cities=["karachi","peshawar","quetta"]
for name in names:
    for city in cities:
        print(name,"belongs to",city)

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end='')
    print()
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end='')
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print("*",end='')
    print()

for i in range(5,0,-1):
    for j in range(1,i+1):
        print("*",end="")
    print()

for i in range(1,6):   #left triangle
    for space in range(5 - i):
        print(" ",end="")
    for star in range(i):
        print('*',end="")
    print()

for i in range(1,6):
    for space in range(5-i):#pyramid shape
        print(" ",end="")
    for star in range(2*i-1):
        print("*",end="")
    print()

    
for i in range(1,6):     
    for space in range(5-i):#diamond shape
        print(" ",end="")
    for star in range(2*i-1):
        print("*",end="")
    print()
for i in range(5,0,-1):
    for space in range(5-i):
        print(" ",end="")
    for star in range(2*i-1):   
        print("*",end="")
    print()

