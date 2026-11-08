from typing import List
from data_classes.Quiz import Quiz
from util.check_a_quiz import check_a_quiz


def check_quizzes(quizzes: List[Quiz]):
    print("===현재 퀴즈 목록===")
    print(f"총 {len(quizzes)}개의 문제가 등록되어 있습니다")
    for idx, item in enumerate(quizzes, 1):
        # 줄바꿈을 막기 위해 end="" 사용
        print(f"\n{idx}번 문제 : ", end="")
        check_a_quiz(item)
    return
