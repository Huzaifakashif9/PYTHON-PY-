import numpy as np
# zeros=np.zeros((2,4))
# print(zeros)

# rng=np.arange(10)
# print(rng)

# #1 d array
# lst=[1,2,3,4,5]

# p=np.array(lst)
# print(type(p))

# #2d array
# l1=[1,2,3]
# l2=[2,3,4]
# l3=np.array([l1,l2])
# print(l3)

# # 3d array
# l4=[1,4,6]
# k=np.array([[l1,l2,l4]])
# print(k)
# print(k.ndim)

# #ones array
# one=np.ones((3,3))
# print(one)

#full array
# full=np.full((2,2),5)
# print(full)

# #identity matrix

# iden=np.eye(2)
# print(iden)

#evenly spaced array
# print(np.arange(1,10,2))

# #equaally spaced array 1 se 10 5 equal hisse mai
# print(np.linspace(1,10,5))

# #random for float
# p=np.random.rand(2,3)
# print(p)

# #random for int pehle kaha se kaha tk then shape of array
# print(np.random.randint(1,10,(2,3)))


# #array index and slicing

# a=np.array([1,2,3,4,5,6,7])
# print(a[2])
# print(a[3])
# print(a[::-1])
# print(a[::2])
# print(a[0:7:3])
# print(a[0:5])
# print(a[-3:])


# h=np.array([[2,3],[4,5],[5,6]])
# print(h[:,0])

a=np.array([1,2,3,5])
b=np.array([1,2,3,4])
# print(np.vstack((a,b)))
# print(np.hstack((a,b)))
print(a==b)
print(np.array_equal(a,b))