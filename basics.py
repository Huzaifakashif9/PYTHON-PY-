num=[10,20,30,40,50]
total=0
for m in num:
    total+=m
avg=total/len(num)
print("average is:",avg)

high=print(max(num))
low=min(num)

passing=[]
for pas in num:
    if pas>=30:
        passing.append(pas)
        print(pas)

students = {
    "Ali": 85,
    "Huzaifa": 92,
    "Sara": 70
}
top=max(students,key=students.get)
print(top,students[top])

for k,v in students.items():
    if v>=80:
        print(k,"has A grade with marks",v)

def login(username,password):
    if username=="admin"and password=="1234":
        print("login succesful")
    else:
        print("invalid creditials")
login("admin","1234")



def game():
    import random

    while True:   
        h = random.randint(1, 10)
        chances = 3

        while chances > 0:
            guess = int(input("Enter a guess (1-10): "))

            if guess == h:
                print("🎉 You won!")
                break
            else:
                chances -= 1
                print("❌ Wrong try. Chances left:", chances)

        if chances == 0:
            print("😢 You are out of chances")
            print("Correct number was:", h)

        y = input("Do you want to play again? (yes/no): ").lower()
        if y == "no":
            print("Okay thanks for playing, bye 👋")
            break
