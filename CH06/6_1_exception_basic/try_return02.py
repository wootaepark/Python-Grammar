# finally 키워드 활용

def write_text_file(filename, text):
    try:
        file = open(filename, "w")
        return
        file.write(text)
    except:
        print("오류가 발생")
    finally:
        file.close()


write_text_file("test.txt", "안녕하세요!") # 파일만 생성되고 write 하지는 않는다.
