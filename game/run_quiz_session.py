import random
from typing import List
from datetime import datetime
from data_classes.Quiz import Quiz
from util.choice import choice
from util.check_int_user_input import check_int_user_input
from data_classes.QuizSessionData import QuizSessionData


def run_quiz_session(quizzes: List[Quiz]):
    max_quizzes: int = len(quizzes)
    how_many_quizzes: int = max_quizzes
    run_quiz_menu = ["순서대로 풀기", "랜덤 순서 풀기", "문제 수 선택"]
    start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    while True:
        print("\n=====퀴즈 풀기 메뉴입니다=====")
        user_input = choice(run_quiz_menu)
        # 데이터 안전을 위해 복사
        # 복사본의 생명주기를 while문 내에 배치함으로써 1회성으로만 사용
        # shuffle, how_many_quizzes는 매번 초기화됨
        quizzes_to_play = quizzes[:]

        if user_input == 3:
            show_current_number_of_quizzes(max_quizzes, how_many_quizzes)
            print("몇 문제를 풀지 선택하세요")
            how_many_quizzes = check_int_user_input(max_quizzes)
            print()
            show_current_number_of_quizzes(max_quizzes, how_many_quizzes)
            continue

        if user_input == 2:
            random.shuffle(quizzes_to_play)
            print("\n문제가 무작위로 섞었습니다")

        # how_many_quizzes 만큼 자르기
        quizzes_to_play = quizzes_to_play[:how_many_quizzes]

        score = 0
        for i, q in enumerate(quizzes_to_play, 1):
            print(f"\n문제 {i}. {q.question}")
            for idx, choice_text in enumerate(q.choices, 1):
                print(f"{idx}) {choice_text}")

            while True:
                print("정답을 입력하세요")
                print("- 힌트 보기(0.5점이 차감됩니다.) : '0' 입력")
                # check_int_user_input 재활용
                # int만 입력 가능한 해당 함수의 규칙에 맞게 하기위해 0 이라는 새로운 선택지를 규칙으로 설정함
                user_ans = check_int_user_input(len(q.choices), 0)
                if user_ans == 0:
                    print(f"\n힌트 : {q.hint}")
                    score -= 0.5
                    print(f"0.5점이 차감되었습니다.\n현재점수:{score}\n")
                    continue
                if user_ans == q.answer:
                    print("정답입니다!")
                    score += 1
                    break
                else:
                    print(f"틀렸습니다. 정답은 {q.answer}번입니다.")
                    break

        print(f"\n퀴즈 종료! 당신의 점수: {score}/{len(quizzes_to_play)}")
        end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        current_quiz_session_data = QuizSessionData(
            start_time, end_time, how_many_quizzes, score
        )
        return current_quiz_session_data


def show_current_number_of_quizzes(max, current):
    print(f"총 문제 개수 : {max}")
    print(f"현재 풀 문제 개수 : {current}")
