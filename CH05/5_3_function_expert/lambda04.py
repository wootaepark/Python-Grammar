# 딕셔너리 오름차순 정렬하기

books = [{
    "제목": "혼공파",
    "가격": 18000
}, {
    "제목": "혼공머+딥",
    "가격": 26000
}, {
    "제목": "혼공자",
    "가격": 24000
}]

# 오름차순
books.sort(key=lambda book : book["가격"])
print(books)

# 내림차순
books.sort(key=lambda book : book["가격"], reverse=True)
print(books)
