# ❓ NumPy kya karta hai?
# NumPy Python ka super-fast library hai jo:
# Numbers
# Arrays
# Matrices
# Data analysis
# ko bohot tez handle karta hai.



import numpy as np

arr = np.array([1,2,3,4])
print(arr)
print(type(arr))

# 2D Array (Matrix)

arr2=np.array([
[1,2,3],
[4,5,6],
[7,8,9]
])
print(arr2)
print(arr2[0,0])
print(arr2[1,2])

# Array Properties
print("dimension are",arr2.ndim)
print("rows&columns are",arr2.shape)
print("total elements are",arr2.size)
print("data type is",arr2.dtype)

# Indexing & Slicing
a=np.array([1,2,3,4,5,6,7,8])
print(a[0])
print(a[::-1])
print(a[0:8:2])

# mathematiucal operation

x=np.array([1,2,3,4,5])
y=np.array([2,4,6,8,10])

print(x+y)
print(x*y)
print(x-y)
print(x+2)


# broadcasting

c=np.array([2,4,6,8])
d=10
print("broadcasting",c+d)


# Important Functions

kk = np.array([10,20,30,40])
print(np.sum(kk))
print(np.mean(kk))
print(np.min(kk))
print(np.max(kk))
print(np.std(kk))

# Shape Change
h = np.array([1,2,3,4,5,6])
a=h.reshape(2,3)
print(a)
print(a.flatten())


# rrandom numbers
print(np.random.rand(5))
print(np.random.randint(1,10,5))


# Sorting & Filtering
a=np.array([1,3,6,8,67,59,35,2,4])
print(np.sort(a))
print(a[a>4])

scores = np.array([45, 67, 89, 34, 72, 90, 55])
print(scores[scores>=60])
print(len(scores[scores>60]))
scores[scores>=50]+=5
print(scores)


marks = np.array([40, 55, 70, 35, 90, 48])
marks[marks>=50]-=5
print(marks)


marks = np.array([45,78,90,33,60])
passed= marks >= 50
print(passed)
print(marks[passed])


k=np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])
avg=np.mean(k,axis=1)
print("average",avg)

topper=np.max(k)
print(f"topper is {topper}")