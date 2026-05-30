# 재귀 함수로 구현한 피보나치 수열(1)

def fibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


print("fibonacci(35) : ", fibonacci(5))
# 굉장히 오래 걸린다.
