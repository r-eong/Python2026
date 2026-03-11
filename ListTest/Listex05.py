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

# 같은 월 넣기
same_month = {}

# 매출이 가장 높은 월
top_month = ""
# 매출이 가장 높은 월의 매출액
top_money = 0

# 매출이 가장 낮은 월
bottom_month = ""
# 매출이 가장 낮은 월의 매출액
bottom_money = 0

print("===== 월별 매출 =====")

# 같은 월끼리 합치기
for t in transactions :
    # print(t[0])
    if t[0] == t[0] :
        same_month['month'] = t[0]
        same_month['money'] = t[1]
    else :
        same_month['month'] = t[0]
        same_month['money'] = t[1]

# 출력
for s in same_month :
    print(f"{s['month']} : {s['money'] :,}원")

print()

# 매출 최대 최소 달 구하기
for s in same_month :
    if s['money'] > top_money :
        top_month = s['month']

    bottom_money = top_money

    if s['money'] < bottom_money :
        bottom_month = s['month']

print(f"최고 매출 월 : {top_month} ({same_month[top_month]})")
print(f"최저 매출 월 : {bottom_month} ({same_month[bottom_month]})")

# 누적 매출액
total_money = 0
# 누적 달 수
totla_month = 0

for total in same_month :
    total_money += total['money']
    totla_month += 1

print(f"월 평균 매출 : {total_money / totla_month :,}원")