from typing import List
from dataclasses import fields
from data_classes.Quiz import Quiz
from .check_quizzes import check_quizzes
from util.choice import choice
from util.check_int_user_input import check_int_user_input
from util.check_a_quiz import check_a_quiz


def add_quiz(quizzes: List[Quiz]):
    while True:
        print("퀴즈 등록 메뉴입니다")
        add_quiz_menu = ["새로운 퀴즈 등록", "현재 퀴즈 목록 확인", "종료"]

        user_input = choice(add_quiz_menu)

        match user_input:
            case 1:
                new_quiz = user_input_quiz()
                quizzes.append(new_quiz)
                print("\n--- 새로운 퀴즈가 등록 되었습니다 ---")
                last_idx = len(quizzes) - 1
                added_quiz = quizzes[last_idx]
                print(f"{last_idx+1}번 : ", end="")
                check_a_quiz(added_quiz)
                return
            case 2:
                check_quizzes(quizzes)
            case 3:
                print("퀴즈 등록을 종료합니다")
                break


def user_input_quiz():
    print("\n--- 새로운 퀴즈 등록 ---")
    keys = [field.name for field in fields(Quiz)]

    new_quiz_data = {}

    for key in keys:

        msg = prompt_msg(key)

        match key:
            case "question" | "hint":
                value = input(f"▶ {msg}: ").strip()
            case "choices":
                choices_row_data = input(f"▶ {msg}: ").strip()
                value = [
                    opt.strip() for opt in choices_row_data.split(",") if opt.strip()
                ]
            case "answer":
                print(msg)
                value = check_int_user_input(len(new_quiz_data["choices"]))

        new_quiz_data[key] = value
    print("-" * 30)

    ensure_user_input_new_quiz(new_quiz_data, keys)

    return Quiz(**new_quiz_data)


def prompt_msg(key: str) -> str:
    msg = f"{key}을(를) 입력하세요"
    match key:
        case "choices":
            msg += " 각 문항은 쉼표로 구분해주세요(예: 사과, 배, 포도)"
        case "answer":
            msg += " (정답 번호 숫자 입력)"

    return msg


def ensure_user_input_new_quiz(new_quiz_data: dict, required_fields: list[str]) -> None:
    missing_fields = required_fields - new_quiz_data.keys()
    if missing_fields:
        raise ValueError(f"누락된 필드: {missing_fields}")
    return
