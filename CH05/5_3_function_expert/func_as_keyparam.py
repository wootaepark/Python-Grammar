# key 키워드 매개변수에 함수 전달하기

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


def get_price(book):
    return book["가격"]


print("# 가장 저렴한 책")
print(min(books, key=get_price))
print()

print("# 가장 비싼 책")
print(max(books, key=get_price))
