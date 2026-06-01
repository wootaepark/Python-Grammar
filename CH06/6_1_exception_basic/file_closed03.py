# finally 구문을 사용해 파일 닫기

try:
    file = open("info.txt", "w")
    예외.발생하기
except:
    print("오류 발생")
finally:
    file.close() # 근데 꼭 finally 로 감쌀 필요가 있을까

print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed : ", file.closed)
