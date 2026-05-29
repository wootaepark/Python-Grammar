# 위치를 통해 리스트 요소 하나 제거하기

list_a = [0, 1, 2, 3, 4, 5]
print("# 리스트의 요소 하나 제거하기")

del list_a[1] # del 키워드를 이용해서 특정 인덱스 요소 지우기
print("del list_a[1] : ", list_a)

del list_a[2:] # 범위 연산을 이용해서 특정 인덱스 뒤 모두 제거
print("del list_a[2:] : ", list_a)

list_a.pop(1) # pop 함수를 이용해서 특정 위치 요소 지우기
print("pop(1) : ", list_a)