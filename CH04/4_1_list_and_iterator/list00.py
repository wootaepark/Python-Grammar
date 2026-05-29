
list_a = [10, 20, "문자열", True, False]

print(list_a[0])
# print(list_a[4][1]) # 오류 발생 (문자형만 가능하다)
print(list_a[2])
print(list_a[2][1])

# 음수 인덱스 접근
print(list_a[-1])
print(list_a[-3][-1])
