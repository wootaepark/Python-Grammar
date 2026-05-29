# 여러 줄 문자열과 if 구문을 조합했을 때의 문제 해결 (2) , join 이용

# 문자열.join(문자열로 구성된 리스트)
# 각 리스트 요소 사이에 문자열을 넣어준다.

number = int(input("정수 입력 > "))

if number % 2 == 0:
    print("\n".join([
        "입력한 문자열은 {} 입니다.", # ',' 를 붙여야 각 행마다 줄바꿈이 된다.
        "{}는 짝수입니다."
    ]).format(number, number)
          )

else:
    print("\n".join([
        "입력한 문자열은 {} 입니다.",
        "{}는 홀수입니다."
    ]).format(number, number)
          )
