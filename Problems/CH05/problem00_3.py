# p 352의 마무리 확인문제 1번

numbers = [1, 2, 3, 4, 5, 6]

# 이렇게 하면 int 값이 들어가서 오류 (numbers 의 값들을 str로 변경해야함)
# print("::".join(numbers))

print("::".join(map(str, numbers)))