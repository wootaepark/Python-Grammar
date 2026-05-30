# 가변 매개변수 함수

# 1. 가변 매개변수는 한개만 사용가능하다
# 2. 가변 매개변수 뒤에는 일반 매개변수가 올 수 없다.

def print_n_times(n, *values):

    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times(3, "안녕하세요", "즐거운", 3)