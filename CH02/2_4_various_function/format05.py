# 부동 소수점 출력하기

output_a = "{:f}".format(52.123)
output_b = "{:15f}".format(-52.123) # 15칸 오른쪽 정렬 (소수 자리수 보다 적은 수면 아무일도 안일어남)
output_c = "{:+15f}".format(52.123)
output_d = "{:+015f}".format(52.123) # 나머지 칸 0으로 채우기



print(output_a)
print(output_b)
print(output_c)
print(output_d)