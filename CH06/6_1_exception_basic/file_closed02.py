# 파일 처리 중간에 예외 발생
# 파일이 제대로 닫히지 않는다.
# finally 구문의 필요성

try:
    file = open("info.txt", "w")
    예외.발생
    file.close()
except:
    print("오류 발생")

print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed : ", file.closed)
