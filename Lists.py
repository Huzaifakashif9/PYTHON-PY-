name=["orange","peach","apple"]
print(name[0])
print(name[-1])
print(name[0:])

#To replace
name[1]="kiwi"
print(name)
name[2]="mango"
print(name)

#To expand ad at last
name.append('orange')
print(name)

#to insert 1st param location 2nd value
name.insert(0,'apple')
print(name)
name.insert(5,'grapes')
print(name)

#to delete remove last one
name.pop()
print(name)

#to sum
x=[1,2,3,4,5,6,7,8]
print(sum(x))

#for average
average=sum(x)/(len(x))
print(average)

#for remove
name.remove("orange")
print(name)
name.remove("mango")
print(name)

#sorting
num=[1,7,4,2,9,5]
num.sort()
print("sorted:",num)

#reverse
num.reverse()
print("reverse:",num)

#using for loop
numbers=[1,2,3,4,5,6,7,8]
total=0
for numb in numbers:
    total+=numb
print("Sum:", total)

#max and min
num1=[2,4,6,8,10]
print("highest marks:",max(num1))
print("lowest marks:",min(num1))

#removing duplicate
huz=[3,4,4,5,5,5,6,6,7,8,8,7,9,9]
n=set(huz)
p=list(n)
print(p)

k=[1,3,5]
l=[2,4,6]
#to combine
combine=k+l
print(combine)

#to combine and sum
combinesum=sum(k)+sum(l)
print(combinesum)

#to combine and sort
bsort=set(combine)
print(bsort)

#list comprehension
xy=[1,2,3,4,5,6]
squares=[x**2 for x in xy]
evennumbers=[ y for y in xy if y%2==0]
print("squares",squares)
print("even numbers",evennumbers)

