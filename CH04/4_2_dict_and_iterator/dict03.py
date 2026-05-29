# 딕셔너리 요소 제거하기

dic = {
    "name" : "박태우",
    "age" : 18
}

print("요소 제거 이전 : {}".format(dic))

del dic["name"]
del dic["age"]
# dic.clear() 해도 된다.

print("요소 제거 이후 : ", dic)