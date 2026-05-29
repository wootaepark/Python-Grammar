# 딕셔너리의 요소 접근

dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치차황색소"],
    "origin": "필리핀"
}

# 출력부
print("name : ", dictionary["name"])
print("type : ", dictionary["type"])
print("ingredient : ", dictionary["ingredient"])
print("origin : ", dictionary["origin"])
print()

# 값 변경
dictionary["name"] = "8D 건조 망고"
print("name : ", dictionary["name"])

# dict 에 값추가
dictionary["manufacturer"] = "person1"
print(dictionary)
print()

# del 키워드를 이용한 특정 값 삭제
del dictionary["name"]
print(dictionary)
