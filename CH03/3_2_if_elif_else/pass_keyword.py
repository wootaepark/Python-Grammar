# 나중에 구현하려고 비워 둔 구문 (에러 난다.)
# 파이썬은 아무것도 안쓰면 에러가 발생한다.

number = int(input("정수 입력 > "))

if number > 0:
    raise NotImplementedError # pass 대신 의도한 오류를 발생시켜 해당 부분의 미구현을 파악 할 수 있다.
# 양수일 때 : 아직 미구현
else:
    pass
# 음수일 때 : 아직 미구현


# 따라서 pass 키워드를 사용해서 아무것도 안하는 조건문임을 표시한다.
