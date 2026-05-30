# 피보나치 수열을 메모 하여 연산을 빠르게 하는 경우

dic = {
    1: 1,
    2: 1,
}


def fibonacci(n):
    if n in dic:
        return dic[n]

    result = fibonacci(n - 1) + fibonacci(n - 2)  # 조기 리턴을 활용하여 else 문을 쓰지 않아도 되도록 함
    dic[n] = result
    return result


print("fibonacci(10) : ", fibonacci(10))
print("fibonacci(50) : ", fibonacci(50))
