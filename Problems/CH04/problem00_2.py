# p 229의 코딩문제 4번

character = {
    "name" : "기사",
    "level" : 12,
    "items" : {
        "sword" : "불꽃의 검",
        "armor" : "풀플레이트"
    },
    "skill" : ["베기", "세게 베기", "아주 세게 베기"]
}
for key in character:
    if type(character[key]) is list:
        for element in character[key]:
            print(f"{key} : {element}")
    elif type(character[key]) is dict:
        for element in character[key]:
            print(f"{element} : {character[key][element]}")
    else:
        print(f"{key} : {character[key]}")



