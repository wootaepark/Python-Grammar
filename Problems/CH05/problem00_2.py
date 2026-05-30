# p 314 의 ch5-2 마무리 1번 문제


# n 명이 각 테이블에 앉을 수 있는 경우의 수
# 최대 10명이 한 테이블에 앉을 수 있다. 테이블당 최소 두명이 앉아야 한다.
min_value = 2
max_value = 10
total = 100

memo = {}


def solve(remain, complete):  # 남은 인원, 앉은 인원
    key = str([remain, complete])

    # 종료 조건
    if key in memo:
        return memo[key]
    if remain < 0:
        return 0
    if remain == 0:
        return 1

    count = 0
    for i in range(complete, max_value + 1):
        count += solve(remain - i, i)

    memo[key] = count
    return count


print(solve(100, min_value)) # 100명이 남아있고 2명은 이미 앉아있다고 가정하는 것
