# 키워드 매개변수 즉 이름을 직접 사용함으로서 의도한 바와 같이 함수를 사용 할 수 있다.


def print_n_times(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()


print_n_times("안녕하세요", "즐거운", "파이썬", n=3)

# n 이라는 키워드 매개변수를 직접 부여함으로서 해결
