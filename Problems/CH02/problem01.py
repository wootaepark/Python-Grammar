# p 152 의 1번 도전 문제
# 구의 부피와 겉넓이

r = int(input("구의 반지름을 입력해주세요: "))

pi = 3.141592
volume = 4 / 3 * pi * r ** 3
extent = 4 * pi * r ** 2
print("= 구의 부피는 {} 입니다.".format(volume))
print("= 구의 겉넓이는 {} 입니다.".format(extent))
