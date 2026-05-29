# p 268 의 도전문제 2번

string = input("염기 서열을 입력해주세요 : ")

dic = {
    "a": 0,
    "t": 0,
    "g": 0,
    "c": 0
}

# ctacaatgtcagtatacccattgcattagccgg

# for i in string:
#    if i not in dic:
#       dic[i] = 0
#    dic[i] += 1

for i in string:
    dic[i] += 1

for i in dic:
    print(f"{i}의 개수 : {dic[i]}")
