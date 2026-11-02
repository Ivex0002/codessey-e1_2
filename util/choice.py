from typing import List


def choice(choices: List[str]):
    print("\n")
    for idx, item in enumerate(choices, 1):
        print(f"{idx}. {item}")
    user_input = input("선택: ").strip()
    return user_input
