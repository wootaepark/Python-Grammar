# p 248 의 2번 손코딩 문제

key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]
character = {}

# 두 리스트를 하나로 조합해 dictionary 로 만들기

for i in range(len(key_list)):
    character[key_list[i]] = value_list[i]

print(character)