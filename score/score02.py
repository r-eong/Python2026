print("=" * 50)
print(f"{"택시 요금 안내": ^45}")
print("=" * 50)

start = input("출발지 : ")
end = input("목적지 : ")
km = float(input("이동 거리(km) : "))
time = int(input("탑승 시간(0 ~ 23시) : "))
baby = input("13세 미만의 어린이 동반 여부(예/아니오) : ")

print("=" * 50)

def_price = 4800

if km <= 2 :
    price = 0
elif km > 2 :
    # 0.1 = 100원
    # 1km = 1000m
    price = ((km - 2)/0.1) * 100
elif baby == "예" :
    if km <= 2 :
        def_price = 0
        price = 0
    else :
        price = (km - 2) * 100 - def_price

# total_price = price

if 22 <= time <= 24 or 1 <= time <= 4 :
    night_price = (def_price + price) * 0.2
else :
    night_price = 0

print(f"기본요금 : {def_price: >10,}원")
print(f"거리요금 : {int(price): >10,}원")
print(f"심야할증 : {int(night_price): >10,}원 (20%)")
print("-" * 50)
print(f"최종요금 : {int(def_price + price + night_price): >10,}원")
print("=" * 50)