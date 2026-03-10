# 이스케이프 문자, 서식문자 이용 영수증 출력
# 파이썬은 변수를 선언할 때 변수선언 명령문이 존재하지 않는다.

# 데이터 준비
order_no = "12345678"
adress = "서울시 종로구 종로3가"
name = "김사장"
phone = "070-1234-5678"

# 품목 데이터(계산식 포함)
# 파이썬은 변수 여러개를 나란히, 상수를 나란히 정의할 수 있다.
# 예) a, b, c = 1, 2, 3
item1, p1, q1 = "블루투스 이어폰", 85000, 1
item2, p2, q2 = "USB 3.0 8G", 8000, 1

# 파이썬 사칙연산자 : +, -, *, /, %
amt1 = p1 * q1
amt2 = p2 * q2
total = amt1 + amt2
received = int(input("낼 금액 입력 : "))
change = received - total

# 출력
# 서식문자는 f-string(현재 표준으로 사용)
# ^ : 가운데정렬
# 45 : 길이 
print(f"{'파이썬 쇼핑몰' : ^45}")
print(f"번호 : {order_no}")
print(f"주소 : {adress}")
print(f"성명 : {name}")
print(f"전화 : {phone}")
print("-" * 60)

# 헤더
# <20 : 20칸 왼쪽정렬
# >20 : 20칸 오른쪽정렬
print(f"{"품명" : <20}{"단가" : >15}{"수량" : >5}{"금액" : >10}")
print("-" * 60)

# 품목 출력시 1000단위마다 콤마 출력 : >10,
print(f"{item1 : <20}{p1 : >15,}{q1 : >7}{amt1 : >10,}")
print(f"{item2 : <20}{p2 : >22,}{q2 : >7}{amt2 : >10,}")

# 하단 결제정보
# 조건 : received 가 total 보다 작으면 "금액이 부족합니다." 아니면, 제대로 출력되도록
print("-" * 60)

if received < total :
    print(f"금액이 부족합니다.{total - received : >41,}")
else :
    print(f"{"소계" : <45}{total : >12,}")
    print(f"{"청구금액":<43}{total : >12,}")
    print(f"{"받은금액":<43}{received : >12,}")
    print(f"{"거스름돈":<43}{change : >12,}")

print("-" * 60)