# 트러블 슈팅

### 숫자/문자열 타입 불일치 문제

```
/e/codyssey/e1_2 (main)
$ python main.py

==============================
   🎯 퀴즈 게임 메뉴
==============================


1. 퀴즈 시작
2. 최고 점수 확인
3. 퀴즈 추가
4. 현재 퀴즈 목록 보기
5. 종료
선택: 1
잘못된 입력입니다. 1~5 사이의 숫자를 입력하세요.

==============================
   🎯 퀴즈 게임 메뉴
==============================


1. 퀴즈 시작
2. 최고 점수 확인
3. 퀴즈 추가
4. 현재 퀴즈 목록 보기
5. 종료
선택: 2
잘못된 입력입니다. 1~5 사이의 숫자를 입력하세요.
```

유틸 함수인 `check_int_user_input`, `choice` 통합 이후 첫 진입점인 `QuizGame` 에서 자연수를 입력했음에도 제대로 분기 처리가 되지 않는 문제가 발생함

- 해결방법

```
user_input = choice(menu)
print(f"user_input : {user_input}, {type(user_input)}") #
```

해당 코드로 `user_input`의 실제 값과 타입을 조사함

```
/e/codyssey/e1_2 (main)
$ python main.py

==============================
   🎯 퀴즈 게임 메뉴
==============================


1. 퀴즈 시작
2. 최고 점수 확인
3. 퀴즈 추가
4. 현재 퀴즈 목록 보기
5. 종료
선택: 1
user_input : 1, <class 'int'>
잘못된 입력입니다. 1~5 사이의 숫자를 입력하세요.
```

int로 출력됨을 확인

=> `game\QuizGame.py` 에서 분기 처리를 `if user_input == "1":` 와 같이 비교중이었음. 즉 숫자 대신 문자열 처리를 하고 있었던 것. 기본적으론 `input` 결과값이 문자열이고, 이를 `check_int_user_input` 함수에선 비교를 위해 `int` 로 전환하여 리턴해주던 것이 문제 원인이었음. 따라서 분기점마다 문자열을 숫자로 변경하면 해결 될것이라 판단함

```
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
```

```
/e/codyssey/e1_2 (main)
$ python main.py

==============================
   🎯 퀴즈 게임 메뉴
==============================


1. 퀴즈 시작
2. 최고 점수 확인
3. 퀴즈 추가
4. 현재 퀴즈 목록 보기
5. 종료
선택: 1
user_input : 1, <class 'int'>
퀴즈 풀기 메뉴입니다


1. 순서대로 풀기
2. 랜덤 순서 풀기
3. 문제 수 선택
선택:
```

- 변경 후 정상적으로 동작함을 확인

### 최상위 폴더 임포팅 문제

[점수 기록 히스토리 로직 구현](https://github.com/Ivex0002/codessey-python/commit/92b72fafdfe55559b7a044f63efabed9bd8f437d) 작성 중, 데이터 정의 클래스와 로직 클래스가 혼합되어 분리 필요성을 느끼고 최상위 폴더에 data_classes 디렉토리 생성 및 `Quiz`, `QuizSessionData` 를 구현함
이 과정에서 먼저 구현되어 있던 `Quiz` 데이터 클래스 파일을 `game` 디렉토리에서 `data_classes` 디렉토리로 이동함
그러나 단순 파일 이동으론 vscode 상에서 완벽하게 경로 처리를 해주지 못해 다음과 같은 문제가 발생함

```py
# 이전 임포팅
# from .Quiz import Quiz

# vscode로 자동 전환된 임포팅
from ..data_classes.Quiz import Quiz
```

```bash
$ python main.py
Traceback (most recent call last):
  File "E:\codyssey\e1_2\main.py", line 1, in <module>
    from game.QuizGame import QuizGame
  File "E:\codyssey\e1_2\game\QuizGame.py", line 9, in <module>
    from ..data_classes.Quiz import Quiz
ImportError: attempted relative import beyond top-level package
```

위와 같은 실행 오류가 발생한 이유는 아래와 같음

- `main.py`에서 `QuizGame`을 `"__main__"` 으로 실행중이고, 이는 `from game.QuizGame import QuizGame` 를 최상위 패키지로 설정함을 의미함
- 그러나 최상위 패키지 위쪽의, `game` 디렉토리 위의 폴더에 접근하고자 하면 루트보다 위쪽에 해당하므로 접근이 정상적으로 되지 않았던 것이었음

=> 따라서, 이를 해결하려면 3가지 정도의 해결책이 가능함

1. 모든 소스코드를 `src` 디렉토리에 삽입, `src`를 루트 패키지로 지정함으로써 내부에 `game`과 `data_classes`, `util` 등을 가짐
   - 이는 추후에 배포를 위한 설정 파일을 추가할때 코어 로직과 설정 파일을 분리함으로써 유용한 방법으로 판단됨
2. 임포팅 경로를 절대 경로로 수정
   - 현재 폴더 구조에서 가장 간편하고 빠르고 쉬운 해결책임
3. 데이터 클래스를 `game` 디렉토리 내부로 이동
   - 현재 루트 패키지가 `game` 이기 때문에 해결은 되나, 파일의 목적성이 분리가 되지 않아 보기 좋지 않고 추후에 `game` 외부 패키지를 운용할경우 또다시 수정이 필요한 방법임
4. 데이터 클래스들을 단일 패키지로 포장하여 `game`에 제공
   - 프론트(터미널)과 백엔드(`game`)이 분리되어 각각 다른 서비스를 제공해야 할 때 2개 모두 하나의 데이터 구조를 공유함으로써 데이터 안정성을 꾀할 수 있겠으나, 위에서 언급했든 큰 프로젝트가 아니므로 닭 잡는 데에 소 잡는 칼을 쓰는 격임

=> 현재 프로젝트에선 크기가 크지 않고, 웹이나 프록시 서버 등 확장성을 염두하지 않았기 때문에 가장 빠르고 간단한 해결책인 **2번 방법**을 채택함

- 수정 예시

```py
from data_classes.Quiz import Quiz # 절대 경로로 수정
```
`..data_classes.Quiz import Quiz`` 를 검색 후 모두 `data_classes.Quiz import Quiz` 으로 일괄 변경하여 문제를 해결함
