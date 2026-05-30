# 재귀함수를 사용한 팩토리얼 구하기

def factorial(n):
    output = n
    if n == 1:
        return 1

    return output * factorial(n - 1)


print("5! : ", factorial(5))
