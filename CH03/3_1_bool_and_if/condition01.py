# \ 를 이용하여 여러줄에 조건을 입력 할 수 있다.

number = input("정수 입력 > ")

last_character = number[-1]

last_number = int(last_character)

if last_number == 0 \
        or last_number == 2 \
        or last_number == 4 \
        or last_number == 6 \
        or last_number == 8:
    print("짝수 입니다.")

if last_number == 1 \
        or last_number == 3 \
        or last_number == 5 \
        or last_number == 7 \
        or last_number == 9:
    print("홀수 입니다.")
