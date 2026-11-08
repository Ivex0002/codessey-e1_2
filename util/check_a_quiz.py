from game.Quiz import Quiz


def check_a_quiz(quiz: Quiz):
    question, choices, answer = quiz.to_dict().values()
    print(question)
    choices_text = ", ".join([f"{idx}번-{item}" for idx, item in enumerate(choices, 1)])
    print(f"답안 : {choices_text}")

    print(f"정답 : {answer}번\n")
    return
