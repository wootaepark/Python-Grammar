# 딕셔너리의 items() 함수와 반복문

dic = {
    "키A": "값A",
    "키B": "값B",
    "키C": "값C",
}

print("# 딕셔너리의 items() 함수")
print("items : ", dic.items())
print()

print("# 딕셔너리의 items() 함수와 반복문 조합하기")

for key, value in dic.items():
    print(f"dic[{key}] = {value}")
