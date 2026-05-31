# 제너레이터 함수

def test():
    print("함수가 호출되었습니다.")
    yield "test" # 함수 내부에 yield 키워드를 사용하면 해당 함수는 제너레이터 함수가 되며 함수 호출 시 내부 코드가 실행되지 않는다.


print("A 지점 통과")
test()

print("B 지점 통과")
test()
print(test())
