# 람다 함수

power = lambda x: x * x
under_3 = lambda x: x < 3

list_input_a = [1, 2, 3, 4, 5]

# map() 함수 이용
output_a = map(power, list_input_a)
print("# map() 함수의 실행 결과")
print("map(power, list_input_a) : ", output_a)
print("map(power, list_input_a) : ", list(output_a))
print()

# filter() 함수 이용
output_b = filter(under_3, list_input_a)
print("# filter() 함수의 실행 결과")
print("filter(under_3, list_input_a) : ", output_b)  # 제너레이터라 값이 예상과 다르게 나온다.
print("filter(under_3, list_input_a) : ", list(output_b))
