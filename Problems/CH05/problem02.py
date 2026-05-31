# 하노이탑 이동 횟수 구하기
count = 0


def hanoi(move, start, target, sub):
    global count
    if move == 1:
        # print(start, "->", target)
        count += 1
    else:
        hanoi(move - 1, start, sub, target)
        count += 1
        # print(start, "->", target)
        hanoi(move - 1, sub, target, start)


n = int(input("원판의 개수를 입력해주세요 : "))
hanoi(n, "A", "C", "B")

def count_function(n):
    return 2 ** n - 1

print("이동 횟수는 {}번 입니다.".format(count_function(n)))
print("이동 횟수는 {}번 입니다.".format(count))
