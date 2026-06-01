# 반복문과 함께 사용하는 경우 (finally)

print("프로그램이 시작되었습니다.")

while True:
    try:
        print("try 구문이 실행되었습니다.")
        break
        print("try 구문의 break 뒤 부분입니다.")
    except:
        print("except 구문이 실행되었씁니다.")
    finally:
        print("finally 구문이 실행되었습니다.") # while 문을 빠져나가도 무조건 실행된다.
    print("while 반복문의 마지막입니다.")

print("프로그램이 종료되었습니다.")