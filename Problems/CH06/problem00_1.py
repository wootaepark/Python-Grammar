# p 380 의 마무리 확인문제 2번

numbers = [52, 273, 32, 103, 90, 10, 275]

print("# (1) 요소 내부에 있는 값 찾기")
print("- {} 는 {} 위치에 있습니다.".format(52, numbers.index(52)))
print()

print("# (2) 요소 내부에 없는 값 찾기")
number = 10000
try:
    print("- {} 는 {} 위치에 있습니다.".format(number, numbers.index(number)))
except ValueError : # 이런 식으로 일어날 수 있는 예외를 같이 적으면 해당 예외에 대해서만 처리한다. 
    print("- 리스트 내부에 없는 값입니다.")
print()

print("정상 종료 됨")
