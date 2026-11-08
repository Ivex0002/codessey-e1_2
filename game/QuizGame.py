import json
import os
from typing import List
from .Quiz import Quiz
from .quizzes import quizzes
from .run_quiz_session import run_quiz_session
from .add_quiz import add_quiz
from .check_quizzes import check_quizzes
from util.choice import choice


class QuizGame:
    def __init__(self):
        self.quizzes: List[Quiz] = []
        self.best_score: float = 0.0
        self.file_path = "state.json"
        self.load_data()

    def load_data(self):
        if not os.path.exists(self.file_path):
            self.set_default_quizzes()
            return

        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.best_score = data.get("best_score", 0)
                self.quizzes = [Quiz(**q) for q in data.get("quizzes", [])]
        except (json.JSONDecodeError, IOError):
            print("⚠️ 데이터 파일이 손상되었습니다. 기본 데이터로 시작합니다.")
            self.set_default_quizzes()

    def save_data(self):
        data = {
            "quizzes": [q.to_dict() for q in self.quizzes],
            "best_score": self.best_score,
        }
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def set_default_quizzes(self):
        self.quizzes = quizzes
        self.save_data()

    def start_quiz(self):
        score = run_quiz_session(self.quizzes)

        if score > self.best_score:
            print("최고 점수 경신!")
            self.best_score = score
            self.save_data()

    def add_quiz(self):
        add_quiz(self.quizzes)
        self.save_data()
        return

    def check_quizzes(self):
        check_quizzes(self.quizzes)
        return

    def run(self):
        while True:
            print("\n" + "=" * 23)
            print("   🎯 퀴즈 게임 메뉴")
            print("=" * 23)

            menu = [
                "퀴즈 시작",
                "최고 점수 확인",
                "퀴즈 추가",
                "현재 퀴즈 목록 보기",
                "종료",
            ]

            user_input = choice(menu)
            # print(f"user_input : {user_input}, {type(user_input)}")

            match user_input:
                case 1:
                    self.start_quiz()
                case 2:
                    print(f"\n현재 최고 점수: {self.best_score}점")
                case 3:
                    self.add_quiz()
                case 4:
                    self.check_quizzes()
                case 5:
                    print("게임을 종료합니다.")
                    self.save_data()
                    break
                case _:
                    print(f"잘못된 입력입니다. 1~{len(menu)} 사이의 숫자를 입력하세요.")
