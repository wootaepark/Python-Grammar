# if 조건문고 여러줄 문자열

number = int(input("정수 입력 > "))

if number % 2 == 0:
    print(f"""입력한 문자열은 {number}입니다.
{number}는 짝수 입니다.""")
else:
    print(f"""입력한 문자열은 {number}입니다.
{number}는 홀수 입니다.""")

# 앞선 문제가 해결은 됐지만 이상한 구조의 코드가 나온다.