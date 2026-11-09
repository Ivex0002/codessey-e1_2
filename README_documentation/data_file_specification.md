# 데이터 파일 설명

# state.json

- 개요 : 모든 장기 데이터를 읽고, 쓰고, 수정하는 파일입니다

### 불러오기
```
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
```
위와 같이 세션 시작시 장기 데이터를 불러옵니다

만약 데이터가 유효하지 않다면 `game\quizzes.py` 의 기본 데이터로 구성토록 만들었습니다

### 저장
```
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
```
`quiz_session_data` 가 있다면 `history` 배열에 붙여서 저장합니다

`quizzes`의 경우 현재 인스턴스에서 사용중인 `self.quizzes` 데이터를 그대로 재활용합니다

`best_score`또한 위와 같습니다

모든 데이터는 기본적으로 덮어쓰기 방식입니다. 가장 구현하기 쉽고, 다루기 쉽기 때문에 이와 같은 방식을 채택했습니다

만약 이를 실제 서비스로 구현한다면 모든 데이터를 덮어쓰는게 아니라 db 측에 crud를 따로 구성하여 동작에 해당하는 데이터들 만을 편집하도록 만들 필요가 있습니다

# 내부 데이터 클래스

- 게임 세션과 장기 저장 파일에서 재활용 되는 데이터 클래스 형식에 대한 설명입니다

### 퀴즈
```
@dataclass
class Quiz:
    question: str
    choices: List[str]
    answer: int
    hint: str

    def to_dict(self) -> dict:
        return asdict(self)
```
반복적인 작업을 회피하고자 `@dataclass` 메서드를 활용했습니다

만약 이를 활용하지 않았다면 다음과 같이 지루하고 현학적인 데이터 정의 작업을 모든 데이터 클래스 마다 해야만 했습니다. `@dataclass`를 활용함으로써 가독성과 편의성을 챙겼다고 보시면 되겠습니다.
```
class Quiz:
    def __init__(self, question, choices, answer, hint):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    def __repr__(self):
        return (
            f"Quiz(question={self.question!r}, "
            f"choices={self.choices!r}, "
            f"answer={self.answer!r}, "
            f"hint={self.hint!r})"
        )
```

해당 데이터 클래스에서 제공하는 각 키들은 다음과 같습니다
```
question: str       # 질문
choices: List[str]  # 답안
answer: int         # 정답
hint: str           # 힌트
```
퀴즈를 풀고 채점하고, 힌트를 보기 위한 필요 최소한의 데이터만 넣었습니다

### 퀴즈 세션
```
@dataclass
class QuizSessionData:
    start_time: str
    end_time: str
    how_many_quizzes: int
    score: float

    def to_dict(self) -> dict:
        return asdict(self)
```
위의 퀴즈 데이터 클래스와 마찬가지로 `@dataclass` 를 활용해 간결히 작성했습니다

각 문제풀이 기록을 장기 저장하기 위한 데이터 구조입니다

해당 데이터 클래스에서 제공하는 각 키들은 다음과 같습니다
```
start_time: str        # 문제 풀이 시작 시각
end_time: str          # 문제 풀이를 끝냈을 때 시각
how_many_quizzes: int  # 몇 문제를 풀었는지
score: float           # 점수
```
보너스 과제에서 요구한대로 각 문제 풀이 시각, 문제를 푼 횟수, 점수등을 매번 기록토록 작성했습니다

`end_time`의 경우 보너스 과제에 없었으나, 문제를 몇분 동안 풀었나 기록하기에는 활용이 가능한 데이터라고 판단해 임의로 넣었습니다

기록 확인 과정에서 `start_time`과 `end_time`을 대조하여 풀이 시간을 계산 할 수 있습니다

이전 `기능목록`의 [5. 퀴즈 삭제하기](https://github.com/Ivex0002/codessey-e1_2/blob/main/README_documentation/feature_list.md#5-%ED%80%B4%EC%A6%88-%EC%82%AD%EC%A0%9C%ED%95%98%EA%B8%B0)에서 언급한 `인덱스 기반 문제 번호`와 같이 문제들을 푼 시간은 `start_time`과 `end_time`에 의존적인 파생 데이터 이기 때문에 따로 키를 나누어 저장하지 않았습니다
