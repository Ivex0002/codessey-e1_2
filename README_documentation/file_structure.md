# File Structure
```
├── data_classes
│   ├── Quiz.py
│   └── QuizSessionData.py
├── game
│   ├── __init__.py
│   ├── add_quiz.py
│   ├── check_quizzes.py
│   ├── QuizGame.py
│   ├── quizzes.py
│   └── run_quiz_session.py
├── util
│   ├── check_a_quiz.py
│   ├── check_int_user_input.py
│   └── choice.py
├── main.py
└── state.json
```
vscode의 확장 프로그램인 [file-combine](https://marketplace.visualstudio.com/items?itemName=therobertsmith.file-combine) 을 활용 했습니다

기반이 되는 데이터 클래스인 `Quiz.py`, `QuizSessionData.py` 는 추후에 재활용될 가능성을 염두하고 따로 분리했습니다(ex: 프론트 웹페이지 구성)

`main.py`의 경우는 실행 주체와 `QuizGame` 세션 인스턴스를 분리하고자 계층을 나누었습니다

추후에 로그인 로직이나, 로컬 설정 파일등을 사용해야 할 때 `game.run()` 에서 인자로 넣어줄 수 있습니다

퀴즈 하나를 보여주거나, 자연수인 유저 입력을 처리하거나, 문자열로 된 여러 선택지를 제시해야 할 때 등 재사용 가능성이 매우 높은 함수들을 `util/` 디렉토리에 넣어놨습니다

이외의 각 퀴즈풀이 세션 내부에서 사용되는 모든 로직은 `game/` 디렉토리에 넣었습니다
