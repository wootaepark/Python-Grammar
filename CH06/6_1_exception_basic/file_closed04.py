# try except 구문 끝난 후 파일 닫기

try:
    file = open("info.txt", "w")
    예외.발생()
except:
    print("오류 발생")

file.close()
print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed : ", file.closed)
