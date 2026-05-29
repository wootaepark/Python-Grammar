# 이차원 리스트 탐색

list_of_list = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [8, 9]
]

for i in list_of_list:
    for j in i:
        print(j, end=" ") # end 를 사용해서 해당 값의 끝 부분 처리 가능
    print()