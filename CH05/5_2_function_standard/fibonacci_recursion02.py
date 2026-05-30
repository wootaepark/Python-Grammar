# 재귀 함수로 구현한 피보나치 수열 (2)

# 피보나치 수열의 연산횟수를 파악하기 위함

counter = 0


def fibonacci(n):
    print("fibonacci({})를 구합니다.".format(n))
    global counter  # 함수 내부에서 외부의 전역변수를 수정하겠다는 의미 (실무 비권장)
    counter += 1

    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(10)
print("---")
print("fibonacci(10) 계산에 활용된 덧셈 횟수는 {}번 입니다.".format(counter))
