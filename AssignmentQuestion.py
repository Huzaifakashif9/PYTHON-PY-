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

pick = [q1, q2, q3, q4, q5]
score = 0

while True:
    k = random.choice(pick)
    print(k['question'])

    for opt in k['options']:
        print("-", opt)

    user_ans = input("enter your answer: ")

    if user_ans.lower() == k['answer'].lower():
        print("correct")
        score += 10

    elif user_ans.lower() == "exit":
        print("thanks for playing quiz")
        print("final score is", score)
        break

    else:
        print("wrong")
        print("correct answer is:", k['answer'])

    print("current score is", score)