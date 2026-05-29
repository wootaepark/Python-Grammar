# if 조건문과 여러 줄 문자열 (1)

number = int(input("정수 입력 > "))

if number % 2 == 0:
    print(f"""\
        입력한 문자열은 {number} 입니다.
        {number} 는 짝수입니다.
""")
else :
    print(f"""\
            입력한 문자열은 {number} 입니다.
            {number} 는 홀수입니다.
    """)

# 의도 하지 않은 띄어쓰기 문자가 나온다.