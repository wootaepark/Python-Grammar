# 예외 객체

try:
    number_input_a = int(input("정수 입력 >"))

    print("원의 반지름 : ", number_input_a)
    print("원의 둘레 : ", 2 * 3.14 * number_input_a)
    print("원의 넓이 : ", 3.14 * number_input_a ** 2)

except Exception as exception: # Exception 은 모든 에외의 부모 클래스이다.
    print("type(exception) : ", type(exception)) # 예외 타입
    print("exception : ", exception) # 예외 발생 메시지
