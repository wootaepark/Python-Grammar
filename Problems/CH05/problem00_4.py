# p 353의 마무리 확인문제 2번

# 람다식과 filter 를 활용한 문제

# numbers = [i for i in range(1, 10 + 1)]

numbers = list(range(1, 10 + 1))
print(numbers)

print("# 홀수만 추출하기")
print(list(filter(lambda x: x % 2 != 0, numbers)))
print()

print("# 짝수만 추출하기")
print(list(filter(lambda x: x % 2 == 0, numbers)))
print()

print("# 제곱해서 50 미만 추출하기")
print(list(filter(lambda x: x ** 2 < 50, numbers)))
