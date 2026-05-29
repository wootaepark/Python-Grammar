import datetime

now = datetime.datetime.now()

if 3 <= now.month <= 5: # 파이썬은 다른 언어와 달리 이렇게 이어서 범위를 지정 할 수 있다.
    print("이번 달은 {}월로 봄입니다!".format(now.month))

if 6 <= now.month <= 8:
    print("이번 달은 {}월로 여름입니다!".format(now.month))

if 9 <= now.month <= 11:
    print("이번 달은 {}월로 가을입니다!".format(now.month))

if 1 <= now.month <= 2 or now.month == 12:
    print("이번 달은 {}월로 겨울입니다!".format(now.month))
