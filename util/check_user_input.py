# 자연수 응답이 기대될때 잘못된 응답이 올 경우 메시지를 출력하는 함수
def check_user_input(user_input, max_number):
    while True:
        if not user_input.isdigit():
            value = input("❌ 숫자로만 입력해주세요: ").strip()
            continue

        int_value = int(value)
        if 1 <= int_value <= max_number:
            return int_value
        print(f"정답은 1 ~ {max_number} 사이의 숫자로 입력해주세요.")
