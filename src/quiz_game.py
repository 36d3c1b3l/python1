from questions import Question


def main():
    print("Welcome to my quiz game!")

    playing = input("Do you want to play? yes/no: ")

    if playing.lower() != "yes":
        quit()

    print("Okay, let's play!")

    score = 0

    questions = [Question("What bash command does let you change directories? ", "cd"),
                Question("What bash command does let you create a file? ", "touch"),
                Question("What bash command does let you create a directory? ", "mkdir"),
                Question("What bash command does show a list of all files in current directory? ", "ls"),
                Question("What bash command does return path to the current directory? ", "pwd")]

    for question in questions:
        question.ask()
        if question.check_answer(input()):
            print("Correct")
            score += 1
        else:
            print("Incorrect")

    print(f"Congratulations! You got {score}/{len(questions)} right")

if __name__ == "__main__":
    main()