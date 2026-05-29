# 피라미드 만들기
# 이등변 삼각형 1, 3, 5, ... 로 개수 늘어나게

output = ""

for i in range(1, 15):
    for j in range(14, i, -1):
        output += " "
    for k in range(0, 2 * i - 1):
        output += "*"
    output += "\n"

print(output)
