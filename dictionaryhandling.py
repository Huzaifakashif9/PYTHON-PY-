import random
q1 = {
    'question': 'What is the capital of france',
    'options': ['paris', 'London', 'Rome'],
    'answer': 'paris'
}

q2 = {
    'question': 'What is the capital of Germany?',
    'options': ['Berlin', 'Madrid', 'Vienna'],
    'answer': 'Berlin'
}

q3 = {
    'question': 'What is the capital of Italy?',
    'options': ['Rome', 'Athens', 'Lisbon'],
    'answer': 'Rome'
}

q4 = {
    'question': 'What is the capital of Japan?',
    'options': ['Tokyo', 'Beijing', 'Seoul'],
    'answer': 'Tokyo'
}

q5 = {
    'question': 'What is the capital of Canada?',
    'options': ['Ottawa', 'Toronto', 'Vancouver'],
    'answer': 'Ottawa'
}
pick=[q1,q2,q3,q4,q5]
score=0
while True:
    comp=random.choice(pick)
    print(comp['question'])

    for opt in comp['options']:
        print("-",opt)

    user_ans=input("enter your answer")

    if user_ans.lower()==comp['answer']:
        print("correct answer")
        score+=25
    elif user_ans.lower=="exit".lower():
        print("exiting thanks for playing")
        print("final score is",score)
        break
    else:
        print("wrong answer")
        print("correct answer is",comp['answer'])
    print("final score is",score)