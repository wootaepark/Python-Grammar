# except02 코드의 발생 가능한 여러 예외를 구분하여 처리하는 프로그램

list_number = [52, 273, 32, 72, 100]

try:
    number_input = int(input("정수 입력 > "))
    print("{} 번째 요소 : {}", number_input, list_number[number_input])

except ValueError :
    print("정수를 입력해주세요")
except IndexError:
    print("리스트의 인덱스를 벗어났습니다.")
