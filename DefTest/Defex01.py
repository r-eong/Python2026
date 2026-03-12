books = [("파이썬 기초", 15000), ("자바의 정석", 25000), ("React 입문", 18000)]
total = 0

def total_price():
    for t, p in books:
        global total

        total += p
        print(f"도서명 : {t}, {p :,}원")

total_price()

print(f"전체 도서 합계 : {total :,}원")