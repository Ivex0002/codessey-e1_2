from dataclasses import dataclass, asdict
from typing import List


@dataclass
class Quiz:
    question: str
    choices: List[str]
    answer: int

    def to_dict(self) -> dict:
        return asdict(self)
