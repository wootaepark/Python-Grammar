# key_in 예제와 달리 value 를 통해서 key 값을 찾기

dic = {
    "name": "박태우",
    "age": 18,
    "gender": "male",
    "origin": "Korea"
}

target_value = input("찾고자 하는 값 입력 : ")

if target_value.isdigit():
    target_value = int(target_value)

found_key = None

for key, value in dic.items(): # items() 를 이용해서 key, value 를 동시에 가져올 수 있다.ㅏ
    if value == target_value:
        found_key = key
        break


if found_key:
    print(f"입력하신 값의 키는 {found_key} 입니다.")
else :
    print("존재하지 않는 키값이다.")

