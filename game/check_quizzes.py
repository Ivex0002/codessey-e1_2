from typing import List
from .Quiz import Quiz
from util.check_a_quiz import check_a_quiz


def check_quizzes(quizzes: List[Quiz]):
    for idx, item in enumerate(quizzes, 1):
        # 줄바꿈을 막기 위해 end="" 사용
        print(f"\n{idx}번 문제 : ", end="")
        check_a_quiz(item)
    return
