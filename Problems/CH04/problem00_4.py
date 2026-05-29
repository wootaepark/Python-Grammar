# p 248의 3번 손 코딩 문제

limit = 10000
i = 1

sum_value = 0

while sum_value < limit:
    sum_value += i
    i += 1

print(f"{i - 1} 를 더할 떄 {limit} 을 넘으며 그때의 값은 {sum_value} 입니다.")
