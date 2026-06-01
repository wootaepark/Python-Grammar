# 모든 예외 잡기 처리 (except03 코드에서 수정)

list_number = [52, 273, 32, 72, 100]

try:
    number_input = int(input("정수 입력 > "))
    print("{} 번째 요소 : {}".format(number_input, list_number[number_input]))
    예외.발생하기()  # 정상 입력 시 무조건 예외 발생
except ValueError as exception:
    print("정수를 입력해주세요")
    print(type(exception), exception)
except IndexError as exception:
    print("리스트의 인덱스를 벗어남")
    print(type(exception), exception)
except Exception as exception: # 마지막 부분에 모든 예외의 부모를 이용해서 프로그램이 죽지 않도록 함 (순서 관계 x, but 가독성 up)
    print("미리 파악하지 못한 예외가 발생")
    print(type(exception), exception)

