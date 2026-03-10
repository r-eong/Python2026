target = input("목표 일 매출액 : ")

max = 0
min = 0

for i in ["월", "화", "수", "목", "금", "토", "일"] :
    money = input(f"{i}요일 매출 : ")

    if target >= money :
        print("  -> 목표 달성")
        okDay += 1
    else :
        print("  -> 목표 미달")
    
    total_money += money

    if i == 0 :
        max = money
        min = money
    else :
        if money > max :
            max = money
        if money < min :
            min = money

print(f"총 매출 : {total_money :,} | 일 평균 : {int(total_money / i) :,}원")
print(f"최고 매출 : {max :,}원 | 최저 매출 : {min :,}원")
print(f"목표 달성 : {okDay}일")