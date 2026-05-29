# 리스트에 요소 추가하기

list_a = [1, 2, 3]

print("# 리스트 뒤에 요소 추가하기")
list_a.append(4)  # 파괴 함수
list_a.append(5)
print(list_a)
print()

print("# 리스트 중간에 요소 추가하기")
list_a.insert(1, 10) # 0번째에 10 추가
print(list_a)

print("# 리스트를 한번에 추가하기")
list_a.extend([10, 20, 30, 40, 50]) # list_a + list_b 는 비파괴적 함수, extend 는 파괴적 함수 (매개변수가 변화함)
print(list_a)