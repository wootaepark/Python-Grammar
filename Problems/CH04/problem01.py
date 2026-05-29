# p 268의 1번 도전 문제
from os.path import join

numbers = [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]

# 위 리스트에서 사용된 숫자의 종류

total = 0
dic = {}

for i in numbers:
    if i not in dic:
        dic[i] = 0
    dic[i] += 1

print("\n".join([
    "{}에서",
    "사용된 숫자의 종류는 {}개 입니다.",
    "참고: {}"
]).format(numbers, total, dic))
