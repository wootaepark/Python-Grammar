# p 269의 3번 도전문제

string = input("염기 서열을 입력해주세요 : ")

dic = {}

for i in range(0, len(string), 3):

    # 풀이 1.
    # codon = string[i:i+3]
    # if len(codon) == 3:
    #   if codon not in dic:
    #       dic[codon] = 0
    #   dic[codon] += 1

    # 풀이 2.
    tmp = ""
    if i + 3 <= len(string):
        for j in range(i, i + 3):
            tmp += string[j]

        if tmp not in dic:
            dic[tmp] = 0
        dic[tmp] += 1

print(dic)
