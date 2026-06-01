# 파일이 제대로 닫혔는지 확인하기


try:
    file = open("info.txt", "w")
    file.write("hello world") # 하지만 파일 close 전 예외가 발생할 수 있다. (해당 예제는 file_closed02)
    file.close()
except:
    print("오류가 발생했습니다.")

print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed : ", file.closed)
