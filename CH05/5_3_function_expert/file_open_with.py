# 파일 열고 닫기

# with 구문이 종료될때 자동으로 파일이 닫힌다.
with open("basic.txt", "w") as file:
    file.write("Hello Python Programming")
