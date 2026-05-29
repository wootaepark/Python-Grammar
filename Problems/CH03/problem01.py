# p 188 의 도전문제 1번
# 간단한 대화 프로그램

import datetime

now = datetime.datetime.now()

string = input("입력 : ")

if "안녕" in string:
    print("> 안녕하세요.")
elif "몇 시" in string:
    print("> 지금은 {}시 입니다.".format(now.hour))
else:
    print(string)
