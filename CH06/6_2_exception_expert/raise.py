# 간단한 raise 를 이용하여 예외를 발생시키고 해당 예외 처리하기

list_a = [1, 2, 3, 4]

try:
    print(f"{list_a[1]}")
    raise NameError("NameError occur")  # 예외 클래스를 만들면 더 자세하기 사용 가능 (클래스 내용은 CH8)
except NameError as exception:
    print("type(exception) : ", type(exception))
    print("exception : ", exception)
except IndexError as exception:
    print("type(exception) : ", type(exception))
    print("exception : ", exception)
except Exception as exception:
    print("type(exception) : ", type(exception))
    print("exception : ", exception)
