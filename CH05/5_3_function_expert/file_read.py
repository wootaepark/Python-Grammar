# read() 함수로 텍스트 읽기

with open("basic.txt", "r") as file: # basic.txt 가 존재해야 실행이 된다.
    content = file.read()

print(content)
