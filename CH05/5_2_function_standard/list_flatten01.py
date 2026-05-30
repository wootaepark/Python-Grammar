# 리스트 평탄화 하기

def flatten(data):
    output = []
    for item in data:
        if type(item) is list:
            output += item # list.extend(b) 와 같은 역할이다. += 연산자는 요소를 하나하나 결합한다.
        else:
            output.append(item) # 요소든 리스트든 dictionary 든 모두 붙인다.
    return output


example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
print("원본 : ", example)
print("변환 : ", flatten(example)) # 3차원 이상을 평탄화 하지 못함

