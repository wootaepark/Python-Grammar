# pass 키워드를 사용하여 숫자로 변환되는 것들만 리스트에 넣기

list_input_a = ["52", "273", "32", "스파이", "103"]

# 반복을 적용
list_number = []
for item in list_input_a:
    try:
        float(item)
        list_number.append(item)
    except: # 노란 줄의 이유 : 모든 예외 발생 시 실행되도록 해서 광범위 하기 때문에 경고 문구가표시된다.
        pass # 아무것도 실행되지 않도록 한다.

print("{} 내부에 있는 숫자는".format(list_input_a))
print("{} 입니다. ".format(list_number))
