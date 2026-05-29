# reversed() 함수와 이터레이터

numbers = [1, 2, 3, 4, 5, 6]
r_num = reversed(numbers)  # iterator 를 r_num 변수에 넣는 것임 (for 효율성) p 265 참고

print("reversed_numbers : ", r_num)

print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))

# 6번 넘어가면 에러
