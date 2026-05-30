# 디폴트 (기본) 매개변수

# 기본 매개변수 뒤에는 일반 매개변수가 올 수 없다. (위치 햇갈리기 때문)

def print_n_times(value, n=2):  # 디폴트 매개변수 설정
    for i in range(n):
        print(value)


print_n_times("Hello") # n 이 없어도 기본 2번 출력
