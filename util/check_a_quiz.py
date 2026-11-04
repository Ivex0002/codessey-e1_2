from game.Quiz import Quiz
from dataclasses import asdict


def check_a_quiz(quiz: Quiz):
    question, choices, answer = asdict(quiz).values()
    print(question)
    choices_text = ", ".join(
        [f"{idx}번 - {item}" for idx, item in enumerate(choices, 1)]
    )
    print(f"답안 : {choices_text}")

    print(f"정답 : {answer}")
    return
