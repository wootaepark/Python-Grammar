# 파일 열고 닫기

file = open("basic.txt", "w") # 같은 디렉토리에 쓰기 모드로 basic.txt 파일이 없으면 만들어진다.

file.write("Hello Python Programming")

file.close()