# 가변 매개변수가 기본 매개 변수보다 앞에 오는 경우 (반대는 안된다.)

def print_n_times(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)

        print()


print_n_times("안녕하세요", "즐거운", "파이썬", 3)
# 의도치 않은 결과로 나오기는 하지만 정상적으로 출력 된다. (기본 매개변수가 무조건 동작하는 현상 발생)
# 이를 해결하기 위한 것이 "키워드 매개변수"
