#1-10
onetoten=[i for i in range(1,11)]
print(onetoten)

#Numbers ke square
sq=[i*i for i in range(1,6)]
print(sq)

#Sirf even numbers
even=[i for i in range(1,10) if i%2==0]
print(even)

#Sirf odd numbers
odd=[i for i in range(1,10) if i%2==1]
print(odd)

#Strings ki length
names = ["Ali", "Ahmed", "Huzaifa"]
k=[len(name) for name in names]
print(k)

#String ko uppercase mai convert karna
names = ["Ali", "Ahmed", "Huzaifa"]
p=[name.upper() for name in names]
print(p)

#Condition ke sath value change karna
nums = [1, 2, 3, 4, 5]
j=[(1,'even'if num %2==0 else 'odd') for num in nums]
print(j)

#List se duplicate remove karna
nums = [1, 2, 2, 3, 4, 4, 5]
he=[i for i in set(nums)]
print(he)

o=[[j for j in range(1,5)]for i in range(3)]
print(o)

#jiski len 4 se above ho list se wo niaklo
names = ["Ali", "Ahmed", "Huzaifa"]
hh=[i for i in names if len(i)>4]
print(hh)

#Filtering (if condition)
data = [10, None, 25, "", 40, 0]
g=[i for i in data if i]
print(g)

#Conditional Transformation
# user=int(input("enter your numnber"))
# ok=["pass"if user>=60 else "fail"]
# print(ok)

#Mapping / Transformation
money=[100,200,300]
kk=[mone*280 for mone in money]
print(kk)

#[1,3][1,4][2,3][2,4]
re=[(x,y)for x in (1,2)for y in (3,4)]
print(re)

k=[(x,y,x*y)for x in range (1,4)for y in range(1,4)]
print(k)

p=[(x,x**2)for x in range(1,6)]
print(p)

j=[(x,y,x*y) for x in range(1,6)for y in range(1,6)if x*y%2==0]
print(j)

text='programmingisfun'
vowels=[ch for ch in text if ch in 'aeiou']
print(vowels)

#dictionary
p={ x:x**2 for x in range(1,6)}
print(p)

words=['pyhton','ai','huzaifa']
l={x:len(x) for x in words}
print(l)

w={'ali':'80','al':'35','kha':'80'}
p={k:v for k,v in w.items() if int(v)>50 }
print(p)

#hello : h
w={"this","is","a","laptop"}
j={x:x[0] for x in w}
print(j)

w=input("enter a word")
vowels='aeiou'
w=[x for x in w if x in vowels]
print(w)