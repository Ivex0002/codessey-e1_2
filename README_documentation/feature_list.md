# 기능 목록

### 0. 메인 진입점 분기
```
PS C:\Users\User\Documents\e1_2> python main.py

=======================
   🎯 퀴즈 게임 메뉴
=======================


1. 퀴즈 시작
2. 최고 점수 확인
3. 퀴즈 추가
4. 현재 퀴즈 목록 보기
5. 퀴즈 삭제하기
6. 종료
선택: 
```
처음 파일을 시작하면 보게 되는 화면입니다.

퀴즈 풀기, 최고 점수 확인 등의 메뉴를 선택할 수 있습니다.

### 1. 퀴즈 시작
```
=======================
   🎯 퀴즈 게임 메뉴
=======================


1. 퀴즈 시작
2. 최고 점수 확인
3. 퀴즈 추가
4. 현재 퀴즈 목록 보기
5. 퀴즈 삭제하기
6. 종료
선택: 1

=====퀴즈 풀기 메뉴입니다=====


1. 순서대로 풀기
2. 랜덤 순서 풀기
3. 문제 수 선택
```
퀴즈 시작 선택시 나오는 화면입니다.

기본 과제인 순서대로 풀기, 보너스 과제인 랜덤 순서 풀기와 문제 수 선택 메뉴가 있습니다.

문제 수 선택의 경우 보너스 과제 설명에서 아무런 제약이 없었으나, ux적인 측면에서 유저의 선택을 저장해 놓았다가 풀기 직전에 splice 하는것이 알맞다 생각해 다음과 같이 로직을 짰습니다
```
def run_quiz_session(quizzes: List[Quiz]):
    max_quizzes: int = len(quizzes)
    how_many_quizzes: int = max_quizzes
    run_quiz_menu = ["순서대로 풀기", "랜덤 순서 풀기", "문제 수 선택"]
    start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    while True:
        print("\n=====퀴즈 풀기 메뉴입니다=====")
        user_input = choice(run_quiz_menu)
        quizzes_to_play = quizzes[:]

        if user_input == 3:
            show_current_number_of_quizzes(max_quizzes, how_many_quizzes)
            print("몇 문제를 풀지 선택하세요")
            how_many_quizzes = check_int_user_input(max_quizzes)
            print()
            show_current_number_of_quizzes(max_quizzes, how_many_quizzes)
            continue

        if user_input == 2:
            random.shuffle(quizzes_to_play)
            print("\n문제가 무작위로 섞었습니다")

        # 말씀드린 파트입니다
        # how_many_quizzes 변수를 저장해 놓았다가 풀기 로직 실행 직전에 splice하여 선택된 개수만큼만 quizzes_to_play에 복사 후 사용합니다
        # 기본 디폴트 값은 인자로서 전달된 quizzes의 길이와 동일합니다
        # 매 세션 실행 시 디폴트 값을 기본으로 사용하고, how_many_quizzes 는 매번 직접 설정토록 구성했습니다
        quizzes_to_play = quizzes_to_play[:how_many_quizzes]
        (중략)
```
