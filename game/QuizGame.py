import json
import os
from typing import List
from data_classes.Quiz import Quiz
from .quizzes import quizzes
from .run_quiz_session import run_quiz_session
from .add_quiz import add_quiz
from .check_quizzes import check_quizzes
from .check_history import check_history
from util.choice import choice
from util.check_a_quiz import check_a_quiz
from util.check_int_user_input import check_int_user_input
from data_classes.QuizSessionData import QuizSessionData


class QuizGame:
    def __init__(self):
        self.quizzes: List[Quiz] = []
        self.best_score: float = 0.0
        self.history: List[QuizSessionData] = []
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
                self.history = [QuizSessionData(**s) for s in data.get("history", [])]
        except (json.JSONDecodeError, IOError):
            print("⚠️ 데이터 파일이 손상되었습니다. 기본 데이터로 시작합니다.")
            self.set_default_quizzes()

    def save_data(self, quiz_session_data: QuizSessionData = None):
        if quiz_session_data:
            self.history.append(quiz_session_data)
        data = {
            "quizzes": [q.to_dict() for q in self.quizzes],
            "best_score": self.best_score,
            "history": [session.to_dict() for session in self.history],
        }
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def set_default_quizzes(self):
        self.quizzes = quizzes
        self.save_data()

    def start_quiz(self):
        quiz_session_data = run_quiz_session(self.quizzes)

        if quiz_session_data.score > self.best_score:
            print("최고 점수 경신!")
            self.best_score = quiz_session_data.score

        self.save_data(quiz_session_data)

    def add_quiz(self):
        add_quiz(self.quizzes)
        self.save_data()
        return

    def check_quizzes(self):
        check_quizzes(self.quizzes)
        return

    def check_history(self):
        check_history(self.history)
        return

    def show_record(self):
        menu = ["현재 등록된 퀴즈 보기", "기록 보기", "뒤로가기"]
        while True:
            print("===퀴즈/기록 보기 메뉴입니다===")
            user_input = choice(menu)

            match user_input:
                case 1:
                    self.check_quizzes()
                case 2:
                    self.check_history()
                case 3:
                    print("퀴즈/기록 보기를 종료합니다")
                    break

    def del_quiz(self):
        print("\n삭제할 문제의 번호를 선택해주세요(취소 : 0)")
        del_user_input = check_int_user_input(len(self.quizzes), 0)
        if del_user_input == 0:
            print("취소되었습니다")
            return

        del_idx = del_user_input - 1

        print("\n!경고!")
        print("삭제할 문제가 맞는지 다시 한번 확인해주세요")
        print(f"\n{del_user_input}번 문제 : ", end="")
        check_a_quiz(self.quizzes[del_idx])
        del_tf = input("\n삭제하시겠습니까? y/n\n입력 :").strip().lower() == "y"
        if del_tf:
            del self.quizzes[del_idx]
            self.save_data()
            print("삭제되었습니다.")

        else:
            print("취소되었습니다")

    def run(self):
        menu = [
            "퀴즈 시작",
            "최고 점수 확인",
            "퀴즈 추가",
            "퀴즈/기록 보기",
            "퀴즈 삭제하기",
            "종료",
        ]
        try:
            while True:
                print("\n" + "=" * 23)
                print("   🎯 퀴즈 게임 메뉴")
                print("=" * 23)

                user_input = choice(menu)
                # print(f"user_input : {user_input}, {type(user_input)}")

                # user_input의 예외 처리는 choice, check_int_user_input 에서 수행합니다.
                match user_input:
                    case 1:
                        self.start_quiz()
                    case 2:
                        print(f"\n현재 최고 점수: {self.best_score}점")
                    case 3:
                        self.add_quiz()
                    case 4:
                        self.show_record()
                    case 5:
                        print("\n!!!퀴즈 삭제 메뉴입니다!!!\n")
                        self.check_quizzes()
                        self.del_quiz()
                    case 6:
                        print("게임을 종료합니다.")
                        self.save_data()
                        break

        except (KeyboardInterrupt, EOFError):
            print("\n\n프로그램 종료 요청이 감지되었습니다.")
            print("데이터를 저장하고 종료합니다.")

            try:
                self.save_data()
                print("데이터 저장이 완료되었습니다.")
            except OSError as e:
                print(f"데이터 저장에 실패했습니다: {e}")

            print("프로그램을 종료합니다.")
