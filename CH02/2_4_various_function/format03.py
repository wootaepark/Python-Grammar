# 기호를 붙여서 출력하기

output_f = "{:+d}".format(32)
output_g = "{:+d}".format(-32)
output_h = "{: d}".format(32) # 부호가 없으면 공백 있으면 부호로 출력하도록 함 
output_i = "{: d}".format(-32)

print("# 기호와 함께 출력하기")
print(output_f)
print(output_g)
print(output_h)
print(output_i)
