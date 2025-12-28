#2d list
m=[
[1,2,3],
[4,5,6],
[7,8,9]
]
m[2][2]
print(m[2][2])

m[2][1]=22    #to change value
print(m)

m.append([10,11,12])     #to expand
print(m)

m[2].append(99)
print(m)
for row in m:
    for column in row:
        print(column,end=' ')
    print()

max=[0][0]
for row in m:
    for column in row:
        if column>max:
           max=column
print("greatest number of list is",max)

 #2D List banana using nest for
matrix=[]
for i in range(0,3):
    row=[]
    for j in range(0,3):
        row.append(j)
    matrix.append(row)
print(matrix)

# #User Se 2D List Input Lena
rows=int(input("enter rows"))
cols=int(input("enter columns"))
matrix=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        val = int(input(f"Enter value for [{i}][{j}]: "))
        row.append(val)
    matrix.append(row)
print(matrix)

#2D List Me Searching (Finding Value)
mat=[[1,2,3,4,5],
    [1,2,3,4,5]]

item=1
found=False
for i in range(len(mat)):
    for j in range(len(mat)):
        if mat[i][j]==item:
            print("found at:",i,j)
            found=True
if not found:
    print("not found")

#2D List Pretty Print (Table Jaise Print Karna)
matrixxx=[[1,2,3,4],
          [5,6,7,8]
]
for row in matrixxx:
    print(" | ".join(map(str, row)))


