transactions = [
    ['2024-01', 3200000],
    ['2024-01', 1500000],
    ['2024-02', 2800000],
    ['2024-02', 900000],
    ['2024-03', 4100000],
    ['2024-03', 2200000],
    ['2024-04', 1800000],
    ['2024-04', 3300000],
    ['2024-05', 5000000],
    ['2024-06', 2100000]
]

# 월별 합산 빈 딕셔너리 생성
# {key: value, key: value}
month_sales = {}

for date, amount in transactions :
    # month_sales 에 이미 해당 월이 존재하면 해당 원에 금액 더해준다
    if date in month_sales :
        month_sales[date] += amount

    # 처음 등장하는 월이면 추가함
    else :
        month_sales[date] = amount

# print(month_sales)
# ┖> {'2024-01': 4700000, '2024-02': 3700000, '2024-03': 6300000, '2024-04': 5100000, '2024-05': 5000000, '2024-06': 2100000}

# 통계 계산을 위한 변수 지정, 최대/최소 변수 지정
max_sales = 0
max_month = ""
min_sales = 0
min_month = ""
total = 0

print("===== 월별 매출 =====")

for month in month_sales :
    # {'2024-01': 4700000, '2024-02': 3700000, '2024-03': 6300000, ...
    # month 는 key('2024-01')라서 아래처럼 쓸 수 있음
    # value(4700000) 값을 찾아서 sales 에 넣음
    # 예) sales = 4700000, sales = 3700000 ... 
    sales = month_sales[month]
    print(f"{month} : {sales :,}원")

    # 총계
    total += sales

    # 최대값, 최대값의 월
    if max_month == "" or sales > max_sales : 
        max_month = month
        max_sales = sales

    # 최소값, 최소값의 월
    if min_month == "" or sales < min_sales :
        min_month = month
        min_sales = sales

# 월 평균 매출
avg = total / len(month_sales)

# 출력
print()

print(f"최고 매출 월 : {max_month} ({max_sales :,}원)")
print(f"최저 매출 월 : {min_month} ({min_sales :,}원)")
print(f"월 평균 매출 : {int(avg) :,}원")