def ask_question(prompt, choices, correct_answer):
    print(prompt)
    for letter, text in choices.items():
        print(f"{letter}) {text}")
    answer = input("Your answer: ").strip().upper()
    print()
    return answer == correct_answer


def easy_questions():
    return [
        (
            "Q1) What does '==' do in Python?",
            {"A": "Assigns a value", "B": "Compares two values", "C": "Creates a function", "D": "Ends a program"},
            "B"
        ),
        (
            "Q2) What type does input() return?",
            {"A": "int", "B": "float", "C": "string", "D": "bool"},
            "C"
        ),
        (
            "Q3) What keyword defines a function?",
            {"A": "func", "B": "def", "C": "define", "D": "function"},
            "B"
        ),
        (
            "Q4) What does 'return' do?",
            {"A": "Stops the program", "B": "Prints output", "C": "Sends a value back", "D": "Creates a loop"},
            "C"
        ),
        (
            "Q5) What is the output of print(3 * 2 + 1)?",
            {"A": "7", "B": "9", "C": "5", "D": "6"},
            "A"
        ),
        (
            "Q6) Which operator performs exponentiation?",
            {"A": "^", "B": "**", "C": "//", "D": "%"},
            "B"
        ),
    ]


def hard_questions():
    return [
        (
            "Q1) What is the output of: print(2 ** 3 ** 2)?",
            {"A": "64", "B": "512", "C": "256", "D": "Error"},
            "B"  # 2 ** 9 = 512
        ),
        (
            "Q2) What does the 'return' keyword do?",
            {"A": "Stops the program", "B": "Prints output", "C": "Sends a value back", "D": "Creates a loop"},
            "C"
        ),
        (
            "Q3) What is the output of: print(len('Python') - 2)?",
            {"A": "4", "B": "5", "C": "3", "D": "6"},
            "A"
        ),
        (
            "Q4) What is the output of: print('5' * 3)?",
            {"A": "15", "B": "555", "C": "Error", "D": "5"},
            "B"
        ),
        (
            "Q5) What does this expression evaluate to: True and False or True?",
            {"A": "True", "B": "False", "C": "None", "D": "Error"},
            "A"
        ),
        (
            "Q6) What is the output of: print(10 // 3)?",
            {"A": "3.33", "B": "3", "C": "4", "D": "Error"},
            "B"
        ),
    ]


def main():
    print("TEST YOUR MIGHT...CODING VERSION")
    print("------------------------------------------\n")

    # Difficulty selection
    print("Choose a difficulty mode:")
    print("1) Easy")
    print("2) Hard")
    mode = input("Enter 1 or 2: ").strip()
    print()

    if mode == "1":
        questions = easy_questions()
        print("You selected EASY mode.\n")
    else:
        questions = hard_questions()
        print("You selected HARD mode.\n")

    total_questions = 0
    num_correct = 0

    # Ask each question
    for prompt, choices, correct in questions:
        total_questions += 1
        if ask_question(prompt, choices, correct):
            num_correct += 1

    # Final Report
    percent = (num_correct / total_questions) * 100

    print("===== QUIZ RESULTS =====")
    print(f"Correct: {num_correct} / {total_questions}")
    print(f"Score: {percent:.2f}%")

    if percent == 100:
        print("Amazing, Wow!")
    elif percent >= 80:
        print("Nice job")
    elif percent >= 60:
        print("Almost ready to code")
    else:
        print("Maybe study next time...")
    print("========================")


main()
