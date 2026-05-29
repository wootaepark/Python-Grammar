# p 270 의 4번 도전 문제

list_2d = [1, 2, [3, 4], 5, [6, 7], [8, 9]]
answer = []

for i in list_2d:
    if type(i) == list:
        for j in i:
            answer.append(j)
    else:
        answer.append(i)

print(
    "\n".join(
        [
            f"{list_2d}를 평탄화 하면",
            f"{answer}입니다."
        ]
    )
)
