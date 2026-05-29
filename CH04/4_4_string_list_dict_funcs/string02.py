# 여러 줄 문자열과 if 구문을 조합했을 때의 문제 해결 (1)

number = int(input("정수 입력 > "))

if number % 2 == 0:
    print((
        f"입력한 문자열은 {number}입니다. \n"
        f"{number}는 짝수 입니다."
    ))
else:
    print((
              "입력한 문자열은 {} 입니다. \n"
              "{}는 홀수 입니다."
          ).format(number, number))


# 이경우는 format 을 사용하는 것이 f 를 중복시키지 않고 자연스럽게 사용 할 수 있을 것 같다.