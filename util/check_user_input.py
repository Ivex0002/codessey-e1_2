# 자연수 응답이 기대될때 잘못된 응답이 올 경우 메시지를 출력
def check_int_user_input(max_number: int, min_number: int = 1):
    while True:
        # x 입력시 뒤로가기 기능?
        user_input = input("선택: ").strip()

        if not user_input.isdigit():
            user_input = input("❌ 숫자로만 입력해주세요: ").strip()
            continue

        int_value = int(user_input)
        if min_number <= int_value <= max_number:
            return int_value

        print(f"정답은 1 ~ {max_number} 사이의 숫자로 입력해주세요.")
