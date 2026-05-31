# 인라인 람다 (람다식 더 간략화)

list_input_a = [1, 2, 3, 4, 5]

output_a = map(lambda x: x * x, list_input_a)
print("# map() 함수의 실행 결과")
print("map(power, list_input_a) : ", output_a)
print("map(power, list_input_a) : ", list(output_a))
print()

output_b = filter(lambda x: x < 3, list_input_a)
print("# filter() 함수의 실행 결과")
print("filter(under_3, list_input_a) : ", output_b)  # 제너레이터라 값이 예상과 다르게 나온다.
print("filter(under_3, list_input_a) : ", list(output_b))
