# 하노이탑 문제

def hanoi(move, start, target, sub):
    if move == 1:
        print(start, "->", target)
    else:
        hanoi(move - 1, start, sub, target)
        print(start, "->", target)
        hanoi(move - 1, sub, target, start)

n = int(input("원판의 개수를 입력해주세요 : "))
hanoi(n, "A", "C", "B")
