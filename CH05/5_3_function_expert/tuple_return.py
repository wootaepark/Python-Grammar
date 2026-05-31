# 여러 개의 값 리턴하기

def test():
    return 10, 20  # 책에서는 괄호로 감싸주었지만 안 감싸도 됨


a, b = test() # 실제로 이와 같이 동작하는 함수가 많다  ex) enumerate(), items(), divmod()

print("a : ", a)
print("b : ", b)
