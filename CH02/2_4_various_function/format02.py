# format 함수를 이용해서 정수를 다양한 방식으로 출력하기

output_a = "{:d}".format(52)
output_b = "{:5d}".format(52)
output_c = "{:05d}".format(52) # 빈칸을 0으로 채우기

# 출력
print(output_a, type(output_a))

# 특정칸에 출력하기
print(output_b, type(output_b))

print(output_c, type(output_c))
