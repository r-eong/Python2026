name = input("이름을 입력하세요 : ")
money = int(input("시급을 입력하세요(원) : "))
time = int(input("하루 근무 시간을 입력하세요(시간) : "))
day = int(input("근무 일수를 입력하세요(일) : "))
start_time = int(input("근무 시간 시간을 입력하세요(0~23) : "))

# 근무시간
work_time = time * day

# 야간근무
if 22 <= start_time <= 24 or 1 <= start_time <= 6 :
    night_work = money * 1.5
else :
    night_work = 0

# 주휴수당
if work_time >= 15 :
    if night_work != 0 :
        add_money = night_work * time * 1
    else :
        add_money = money * time * 1
else :
    add_money = 0

# 기본급
if night_work == 0 :
    def_money = work_time * money
elif night_work != 0 :
    def_money = night_work * work_time
elif add_money == 0:
    def_money = work_time * money
else :
    def_money = add_money * money

# 총 합
total_money = def_money + add_money

# 세금
vat_money = total_money/100*3.3

# 실수령액
final_money = total_money - vat_money

print("=" * 50)
print("급여 명세서")
print("=" * 50)
print(f"이름 : {name}")
print(f"시급 : {money:,}원")
print(f"근무시간 : {work_time}시간 ({time}h x {day}일)")

if night_work == 0 :
    print(f"야간근무 : 해당 없음")
else :
    print(f"야간근무 : 해당 있음 ({int(night_work):,}원 적용)")

if add_money == 0 :
    print(f"주휴수당 : 해당없음")
else :
    print(f"주휴수당 : 해당있음")

print("=" * 50)
print(f"기본급 : {int(def_money):,}원")
print(f"주휴수당 : {int(add_money):,}원")
print(f"세금 : {int(vat_money):,}원")
print("-" * 50)
print(f"실수령액 : {int(final_money):,}원")
print("=" * 50)