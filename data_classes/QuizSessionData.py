from dataclasses import dataclass, asdict


@dataclass
class QuizSessionData:
    start_time: str
    end_time: str
    how_many_quizzes: int
    score: float

    def to_dict(self) -> dict:
        return asdict(self)
