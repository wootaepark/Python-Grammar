# 문자열 양 옆 공백 제거하기

# 좌측의 공백만 제거

s = "   안녕 나는 파이썬을 배우는 중이야    "

print("원본 : ", s)
print("좌측 제거 :", s.lstrip())
print("우측 제거 : {} 확인용 문자".format(s.rstrip()))
print("전체 제거 : {} 확인용 문자".format(s.strip()))
