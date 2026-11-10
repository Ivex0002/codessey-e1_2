from typing import List
from data_classes.QuizSessionData import QuizSessionData
from util.check_a_history import check_a_history


def check_history(history: List[QuizSessionData]):
    print("\n===기록===")
    print(f"총 {len(history)}개의 기록이 등록되어 있습니다")
    for idx, item in enumerate(history, 1):
        print(f"\n{idx}번 기록")
        check_a_history(item)
    return
