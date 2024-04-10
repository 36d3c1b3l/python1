from questions import Question

print("Welcome to my quiz game!")



playing = input("Do you want to play? yes/no: ")

if playing.lower() != "yes":
    quit()

print("Okay, let's play!")

score = 0



question = "What bash command does let you change directories? "
answer = "cd"
question1 = Question(question, answer)

question = "What bash command does let you create a file? "
answer = "touch"
question2 = Question(question, answer)

question = "What bash command does let you create a directory? "
answer = "mkdir"
question3 = Question(question, answer)

question = "What bash command does show a list of all files in current directory? "
answer = "ls"
question4 = Question(question, answer)

question = "What bash command does return path to the current directory? "
answer = "pwd"
question5 = Question(question, answer)



questions = [question1,
             question2,
             question3,
             question4,
             question5]

for question in questions:
    question.ask()
    if question.check_answer(input()):
        print("Correct")
        score += 1
    else:
        print("Incorrect")

print("Congratulations! You got " + str(score) + "/" + str(len(questions)) + " right")

