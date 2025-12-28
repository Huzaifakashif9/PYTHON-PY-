# try:
#     x=int(input("enter a number"))
#     print(10/x)
# except:
#     print("sahi number dalo")

# try:
#     x=int(input("enter a number:"))
#     print(10/x)
# except ZeroDivisionError:
#     print("cant be divide by 0")
# except ValueError:
#     print("number only")
# else:
#     print("no error")
# finally:
#     print("me to chalunga hi chlunga")

try:
    with open("data.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("no file")
finally:
    print("on scence")

n=[1,2,3]
try:
    h=int(input("enter index:"))
    print(n[h])
except IndexError:
    print("index out of range")
except ValueError:
    print("number only")
else:
    print("no error")
finally:
    print("mei to run hunga hi hunga")

std={"name":"huzaifa","age":19}
try:
    key=input("enter key:")
    print(std[key])
except:
    print("key does not exist")
