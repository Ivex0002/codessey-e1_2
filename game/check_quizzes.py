from typing import List
from .Quiz import Quiz


def check_quizzes(quizzes: List[Quiz]):
    for idx, item in enumerate(quizzes, 1):
        print(f"{idx}번 : {item}")
    return
