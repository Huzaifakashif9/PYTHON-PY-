def check(chance,secret_number):
    chance-=1
    if chance>0:
        print("tries left",chance)
    else:
        print("game over!thanks for playing")
        print(f"your correct answer was {secret_number}")
        print("your score is 0")
    return chance



import random
while True:
    print("welcome to guessing game")
    print("choose a difficulty level")
    print("1.Easy (range1-10) (tries5)")
    print("2.Medium (range1-20) (tries4)")
    print("3.Hard (range1-30) (tries3)")

    choice=input("Enter your choice of level")

    if choice=='1':
        max_num=10
        tries=5
        score=10

    elif choice=='2':
        max_num=20
        tries=4
        score=25

    elif choice=='3':
        max_num=30
        tries=3
        score=50

    else:
        print("invalid choice:continue to easy level")
        max_num=10
        tries=5
        score=10

    secret_number=random.randint(1,max_num)
    chance=tries

    while chance>0:
        guess=int(input("enter any number"))

        if guess==secret_number:
            print("you guessed it right")
            points=score*chance
            print(f"your score is {points}")
            break

        elif guess>secret_number:
            print("too high guess")
            chance=check(chance,secret_number)

        elif guess<secret_number:
            print("too low guess")
            chance=check(chance,secret_number)
    
    play_again=input("do you wanty to play again yes/no").lower()
    if play_again=="no":
        print("okay thanks for playing bye")
        break