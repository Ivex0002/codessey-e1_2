import random


def run_quiz_session(quizzes):
    print("\n1. 순서대로 풀기")
    print("2. 랜덤 순서 풀기")
    choice = input("선택: ").strip()

    quizzes_to_play = quizzes[:]
    if choice == "2":
        random.shuffle(quizzes_to_play)
        print("\n문제가 무작위로 섞었습니다")

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
