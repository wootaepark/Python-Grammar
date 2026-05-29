# p 189의 2번 문제
# 나누어 떨어지는 숫자

num = int(input("정수를 입력해주세요 : "))

if num % 2 != 0:
    print("{}은 2로 나누어 떨어지는 숫자가 아닙니다.".format(num))
else:
    print("{}은 2로 나누어 떨어지는 숫자입니다.".format(num))

if num % 3 != 0:
    print("{}은 3으로 나누어 떨어지는 숫자가 아닙니다.".format(num))
else:
    print("{}은 3으로 나누어 떨어지는 숫자입니다.".format(num))

if num % 4 != 0:
    print("{}은 4로 나누어 떨어지는 숫자가 아닙니다.".format(num))
else:
    print("{}은 4로 나누어 떨어지는 숫자입니다.".format(num))

if num % 5 != 0:
    print("{}은 5로 나누어 떨어지는 숫자가 아닙니다.".format(num))
else:
    print("{}은 5로 나누어 떨어지는 숫자입니다.".format(num))
