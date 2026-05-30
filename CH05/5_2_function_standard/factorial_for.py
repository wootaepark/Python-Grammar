# 반복문으로 팩토리얼 구하기

def factorial(n):
    output = 1
    for i in range(1, n + 1):
        output *= i

    return output


print("5! : ", factorial(5))
