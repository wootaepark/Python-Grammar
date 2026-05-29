# 소수점 아래 자릿수 지정하기
output_a = "{:15.3f}".format(52.123)
output_b = "{:15.2f}".format(52.123)
output_c = "{:15.1f}".format(52.123)
output_d = float(output_b)

print(output_a, type(output_a))
print(output_b, type(output_b))
print(output_c, type(output_c))
print(output_d, type(output_d))
