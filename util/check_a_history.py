from data_classes.QuizSessionData import QuizSessionData


def check_a_history(history: QuizSessionData):
    obj = {
        "시작시간": history.start_time,
        "종료시간": history.end_time,
        "푼 문제 수": history.how_many_quizzes,
        "점수": history.score,
    }

    for key, value in obj.items():
        print(f"{key} : {value}")
    return
