import inspect
from typing import List
from data_classes.Quiz import Quiz
from .check_quizzes import check_quizzes
from util.choice import choice


def add_quiz(quizzes: List[Quiz]):
    while True:
        print("퀴즈 등록 메뉴입니다")
        add_quiz_menu = ["새로운 퀴즈 등록", "현재 퀴즈 목록 확인", "종료"]

        user_input = choice(add_quiz_menu)

        if user_input == "1":
            new_quiz = user_input_quiz()
            quizzes.append(new_quiz)
            print("\n--- 새로운 퀴즈가 등록 되었습니다 ---")

            last_idx = len(quizzes) - 1
            added_quiz = quizzes[last_idx]

            print(f"{last_idx+1}번 : {added_quiz}")
            return
        elif user_input == "2":
            check_quizzes(quizzes)
        elif user_input == "3":
            print("퀴즈 등록을 종료합니다")
            break

        else:
            print(
                f"잘못된 입력입니다. 1~{len(add_quiz_menu)} 사이의 숫자를 입력하세요."
            )


def user_input_quiz():
    print("\n--- 새로운 퀴즈 등록 ---")
    sig = inspect.signature(Quiz.__init__)
    params = sig.parameters

    new_quiz_data = {}

    for name, _ in params.items():
        if name == "self":
            continue

        prompt_msg = f"{name}을(를) 입력하세요"

        if name == "choices":
            prompt_msg += " 각 문항은 쉼표로 구분해주세요(예: 사과, 배, 포도)"
        elif name == "answer":
            prompt_msg += " (정답 번호 숫자 입력)"

        value = input(f"▶ {prompt_msg}: ").strip()

        if name == "choices":
            value = [opt.strip() for opt in value.split(",") if opt.strip()]
        elif name == "answer":
            while True:
                if not value.isdigit():
                    value = input("❌ 숫자로만 입력해주세요: ").strip()
                    continue

                int_value = int(value)

                if 1 <= int_value <= len(new_quiz_data["choices"]):
                    value = int_value
                    break
                else:
                    print(
                        f"정답은 1 ~ {len(new_quiz_data['choices'])} 사이의 숫자로 입력해주세요."
                    )
                    value = input("▶ 다시 입력해주세요: ").strip()

        new_quiz_data[name] = value
    print("-" * 30)
    return Quiz(**new_quiz_data)
