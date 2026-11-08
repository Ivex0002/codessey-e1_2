import random
from util.choice import choice
from util.check_user_input import check_int_user_input


def run_quiz_session(quizzes):
    max_quizzes: int = len(quizzes)
    how_many_quizzes: int = max_quizzes
    run_quiz_menu = ["순서대로 풀기", "랜덤 순서 풀기", "문제 수 선택"]

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

            try:
                user_ans = int(input("정답 번호 입력: "))
                if user_ans == q.answer:
                    print("정답입니다!")
                    score += 1
                else:
                    print(f"틀렸습니다. 정답은 {q.answer}번입니다.")
            except ValueError:
                print("숫자만 입력해주세요! 이번 문제는 틀린 것으로 처리됩니다.")

        print(f"\n퀴즈 종료! 당신의 점수: {score}/{len(quizzes_to_play)}")
        return score


def show_current_number_of_quizzes(max, current):
    print(f"총 문제 개수 : {max}")
    print(f"현재 풀 문제 개수 : {current}")
