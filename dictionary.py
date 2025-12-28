# example
x={"name":"huzaifa","age":18}

# access values
print(x["name"])
# using get
print(x.get("job","no job"))  

# ADD
d={}
d["id"]=102
print(d)

# UPDATE
d["id"]=103
print(d)

# to delete
p={'name':"ali","age":19,"school":"kps"}
p.pop('name')
print(p)

# to remove last key
std={"name":"ali","age":19}
std.popitem()
print(std)


# to call keys
std.keys()

# to call values
std.values()
std.items()
print(std)

# nested dicts
std={
    "u1":{"name":"ali","age":18},
    "u2":{"names":"alis","ages":108}
}
print(std['u2']['names'])

# words ka count

hel="i love python and i love dotnet"
word=hel.split()
freq={}
for w in word:
    freq[w]=freq.get(w,0)+1
print(freq)