# p 153 의 2번 도전 문제
# 피타고라스의 정리

w = float(input("밑변의 길이를 입력해주세요: "))
h = float(input("높이의 길이를 입력해주세요: "))

answer = (w ** 2 + h ** 2) ** 0.5

print("= 빗변의 길이는 {:.1f} 입니다.".format(answer))
