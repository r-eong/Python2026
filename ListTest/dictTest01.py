# 딕셔너리 = 오브젝트
# key : value 가 쌍으로 존재
# 딕셔너리 출력방법 : dict["key"]
# dict.key 로 출력불가
# phone_book = {"name": "홍길동", "age": 7, "class": "고급"}

phone_book = {}
phone_book["홍길동"] = "010-1234-5678"
phone_book["강감찬"] = "010-1111-2222"
phone_book["이순신"] = "010-9876-5432"

# 전체출력
print(phone_book)
# 모든 key 만 출력
print(phone_book.keys())
# 모든 value 만 출력
print(phone_book.values())

# ------------------------------------------------

# 문제
# phone_book 를 강감찬 010-1111-1111 이런 방향으로 출력시키시오
# 단, for문 사용
for book in phone_book.keys() :
    print(book, phone_book[book])