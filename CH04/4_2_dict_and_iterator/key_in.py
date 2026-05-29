# 키가 존재하는지 확인하고 값에 접근하기

dic = {
    "name" : "박태우",
    "age" : 18,
    "gender" : "male",
    "origin" : "Korea"
}

key = input("접근하고자 하는 키 : ")

if key in dic:
    print(dic[key])
else :
    print("존재 하지 않는 키에 접근 중입니다.")