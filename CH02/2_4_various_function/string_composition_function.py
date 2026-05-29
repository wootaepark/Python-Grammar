# 문자열 구성 파악하는 함수 모음


s = "Hello I am Python Master 123"
t = "Bye123"
u = "init"
v = "   "
w = "123"

print(t.isalnum()) # 문자열이 알파벳 숫자로만 구성되어 있는지 확인 (공백도 안된다.)
print(s.isalpha()) # 알파벳으로만 되어 있는지
print(u.isidentifier()) # 식별자로 사용 할 수 있는것인지 확인 (변수가 가능한지)
print(v.isspace()) # 공백으로만 이루어져 있는지
print(w.isdecimal()) # 정수형태인지
print(w.isdigit()) # 숫자로 인식될 수 있는지

