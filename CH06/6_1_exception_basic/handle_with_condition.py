# 조건문으로 예외 처리하기

user_input_a = input("정수 입력 > ")

if user_input_a.isdigit():  # 숫자로만 구성되어 있는 경우 (실수도 포함시키지 않는다. 2.4 는 '.' 이 포함됨)
    number_input_a = int(user_input_a)

    print("원의 반지름 : ", number_input_a)
    print("원의 둘레 : ", 2 * 3.14 * number_input_a)
    print("원의 넓이 : ", 3.14 * number_input_a ** 2)

else:
    print("정수를 입력하지 않았습니다.")
