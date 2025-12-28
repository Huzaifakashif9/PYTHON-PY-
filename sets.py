# automatic remove duplicate
s={1,2,2,3,3}
print(s)

s.add(4)
print(s)

s.update([4,5])
print(s)

s.remove(5)

# Union
a={1,2,3}
b={4,5,6}
print(a|b)

# intersection comon values
a={1,2,3,4}
b={3,4,5,6}
print(a&b)

# difference a mein hai b mei nhi
a={1,2,3,4}
b={3,4,5,6}
print(a-b)

# symetric diff jo comon nhi
a={1,2,3,4}
b={3,4,5,6}
print(a^b)


ali={1,2,2,4,4,6}
unique=set(ali)
print(unique)