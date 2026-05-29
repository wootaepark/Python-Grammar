# 문자열 찾기

output_a = "안녕안녕하세요".find("안녕")

print(output_a)  # 처음 찾은 곳의 위치를 반환

output_b = "안녕안녕하세요".rfind("안녕")

print(output_b)  # 뒤 부터 찾은 곳의 위치를 반환

output_c = "안녕안녕하세요".find("잘가세요")

print(output_c) # 없으면 -1 반환
