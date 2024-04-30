




print("*************************")
print("Welcome to My Quiz Game!!!")

question_bank = [
    {"text": "Python is Known as _", "answer": "B"},
    {"text": "Which of these data types does Python not natively support?", "answer": "C"},
    {"text": "Which of the following is not a Python built-in data type?", "answer": "B"},
    {"text": "Which function is used to read input from the console in Python?", "answer": "A"},
    {"text": "What is the purpose of an if statement in Python?", "answer": "B"}
]

options = [
    ["A. Compiled Language", "B. Interpreted Language", "C. Machine Language", "D. Assembly Language"],
    ["A. Lists", "B. Tuples", "C. Arrays", "D. Dictionaries"],
    ["A. Dict", "B. Array", "C. Set", "D. Frozenset"],
    ["A. input()", "B. read()", "C. scan()", "D. getinput()"],
    ["A. to loop through a sequence", "B. to execute a block conditionally", "C. to define a function", "D. to handle exceptions"]
]

score = 0

def check_answer(user_guess, correct_answer):
    return user_guess == correct_answer

for question_num in range(len(question_bank)):
    print("***********************************")
    print(question_bank[question_num]["text"])

    for i in options[question_num]:
        print(i)

    guess = input("Enter Your Answer(A/B/C/D): ").upper()
    is_correct = check_answer(guess, question_bank[question_num]["answer"])
    if is_correct:
        print("Correct Answer")
        score += 1
    else:
        print("Incorrect Answer")

    print((f"Your Correct Score is {question_num+1}/{score}"))    

print("Your final score is:", score)

print(f"Your Score is {(score/len(question_bank))*100}%")





