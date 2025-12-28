# #math module
# import math
# print(math.sqrt(16))
# print(math.pow(3,3))
# print(math.floor(3.4))
# print(math.ceil(3.4))


# #TIME MODULE
# import time
# print(time.time())
# current_time=time.localtime()
# print(current_time)
# for i in range(5,0,-1):
#     print(i,"countdown")
#     time.sleep(1)

# #datetime module
# from datetime import datetime
# print(datetime.now())

# now = datetime.now()
# print(now.strftime("%d-%m-%Y %H:%M:%S"))
# # %d → Day
# # %m → Month
# # %Y → Year
# # %H → Hour (24h)
# # %I → Hour (12h)
# # %p → AM/PM

# #os module
# import os

# current_directory = os.getcwd()
# print(current_directory)

# #statss module
# import statistics

# data = [10, 20,20, 30, 40, 50]
# print(statistics.mean(data))
# print(statistics.median(data))
# print(statistics.mode(data))


#string module
import string 
a='a32b'
for i in a:
    if i in string .digits:
        print(i,'is a digit')
    else:
        print(i,'is a character')

u=input("enter a password")
for i in u:
    if i in string.punctuation:
        print(i,"is a special character")
    elif i in string.digits:
        print(i,'is digit')
    else:
        print(i,'is a character')
k=input("enter a pass")
for i in k:
    if i!=string.punctuation and i!=len(i)>7:
        print("invalid password")
        break
    else:
        print("valid password")
        break

