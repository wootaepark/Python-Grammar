# if 조건문과 긴 문자열

# 해결 법 1 '\n' 을 이용한 개행문자

number = int(input("정수 입력 > "))

if number % 2 == 0:
    print(f"입력한 문자열은 {number} 입니다. \n{number}는 짝수입니다.")
else:
    print(f"입력한 문자열은 {number} 입니다. \n{number}는 홀수입니다.")
