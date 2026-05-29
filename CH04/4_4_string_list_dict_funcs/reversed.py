# reversed 함수


list_a = [1, 2, 3, 4, 5]
# list_a.reverse() 는 원본이 바뀌고 어디에 대입해도 대입당한 변수는 변하지 않는다.
# list_reversed = list_a.reverse()

list_reversed = reversed(list_a)

print("# reversed() 함수")
print("reversed([1,2,3,4,5] : ", list_reversed) # 기본적으로 iterator 를 반환한다.
print("list(reversed([1,2,3,4,5])) : ", list(list_reversed))
print()

# 반복문 적용
print("# reversed() 함수와 반복문")
print("for i in reversed([1,2,3,4,5]) : ")
for i in reversed(list_a):
    print("-", i)
