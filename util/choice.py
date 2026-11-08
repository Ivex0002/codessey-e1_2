from typing import List
from util.check_user_input import check_int_user_input


# 선택지 문자열 배열을 받고 자동으로 번호 출력 및 유저입력 받기
def choice(choices: List[str]):
    print("\n")
    for idx, item in enumerate(choices, 1):
        print(f"{idx}. {item}")
    user_input = check_int_user_input(len(choices))
    return user_input
