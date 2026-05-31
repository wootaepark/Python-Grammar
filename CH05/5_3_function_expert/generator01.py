# 제너레이터 객체과 next() 함수
# 사용 목적 : 함수의 코드를 조금씩 실행할 때 사용 (메모리의 효율성을 위함)

def test():
    print("A 지점 통과")
    yield 1
    print("B 지점 통과")
    yield 2
    print("C 지점 통과")


output = test()
print("D 지점 통과")
a = next(output) # next 호출 시에 yield 전까지 실행되고 yield 키워드 뒤 값이 리턴된다.
print(a)
print("E 지점 통과")
b = next(output)
print(b)
print("F 지점 통과")
c = next(output)

# 아래 두 줄 부터 오류 발생 ( next() 호출 이후 yield 키워드를 만나지 못하고 함수가 끝나는 경우)
print(c)
next(output)
