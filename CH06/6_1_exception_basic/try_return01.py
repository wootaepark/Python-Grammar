# try 구문 내부에서 return 키워드를 사용하는 경우 (이때 사용했을 때 위력을 발휘한다.)

def test():
    print("test() 함수의 첫 줄입니다.")
    try:
        print("try 구문이 실행 됨")
        return
        print("try 구문의 return 키워드 뒤")
    except:
        print("except 구문이 실행 됨")
    else:
        print("else 구문이 실행 됨")
    finally:
        print("finally 구문이 실행 됨")  # 비록 리턴 이후라도 이 구문은 무조건 실행된다
    print("test() 함수의 마지막 줄입니다.")

test()
