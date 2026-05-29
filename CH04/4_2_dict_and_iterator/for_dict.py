# for 반복문과 딕셔너리

dic = {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    "ingredient" : ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin" : "필리핀"
}

for key in dic.keys(): # dic 만 써도 key 값 모두 불러온다.
    print(f"key : {dic[key]}")