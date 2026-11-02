from typing import List
from .Quiz import Quiz

quizzes: List[Quiz] = [
    Quiz("Python의 창시자는?", ["Guido", "Linus", "Bjarne", "James"], 1),
    Quiz(
        "바위너구리와 유전학적으로 가장 가까운 동물은?",
        ["코끼리", "너구리", "오소리", "개"],
        1,
    ),
    Quiz("소의 위장은 몇개인가?", ["1", "2", "3", "4"], 4),
    Quiz(
        "흰개미는 분류상 어떤 생물인가?",
        ["개미목", "벌목", "바퀴목", "집게벌레목"],
        3,
    ),
]
