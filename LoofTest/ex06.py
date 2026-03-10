# if @ in email : email 에 @ 가 포함 되었는지
# if @ not in email : email 에 @ 가 포함되지 않은 것
# for i in [1, 2, 3, 4, 5] : i=1, i=2, i=3, i=4, i=5 
# if grade not in [1, 2, 3, 4, 5] : grade 1, 2, 3, 4, 5 를 제외한 것

# 건수 누적
cnt = 0
# 총 구매금액 누적
total_money = 0
# 총 할인금액 누적
total_discount = 0
# 총 결제금액 누적
total_pay = 0

# 종료
# user_level = "END"

while True :
    user_level = input("회원 등급 : ").upper()

    if user_level == "END" :
        break
    
    user_amount = int(input("구매 금액 : "))

    print()

    if user_level == "BRONZE" :
        print(f"구매 금액 : {user_amount}")
        print(f"할인 없음 -> 지불 금액 : {user_amount :,}원")
        total_discount += 0
        total_pay += user_amount
    elif user_level == "SILVER" :
        print(f"구매 금액 : {user_amount}")
        print(f"할인 금액 : {user_amount*0.05 :,}원 -> 지불 금액 : {user_amount - user_amount*0.05 :,}원")
        total_discount += user_amount*0.05
        total_pay += user_amount - user_amount*0.05
    elif user_level == "GOLD" :
        print(f"구매 금액 : {user_amount}")
        print(f"할인 금액 : {user_amount*0.1 + 5000 :,}원 -> 지불 금액 : {user_amount - (user_amount*0.1 + 5000) :,}원")
        total_discount += user_amount*0.1 + 5000
        total_pay += user_amount - (user_amount*0.1 + 5000)
    elif user_level == "VIP" :
        print(f"구매 금액 : {user_amount}")
        print(f"할인 금액 : {user_amount*0.2 + 10000 :,}원 -> 지불 금액 : {user_amount - (user_amount*0.2 + 10000) :,}원")
        total_discount += user_amount*0.2 + 10000
        total_pay += user_amount - (user_amount*0.2 + 10000)
    else :
        print("등록되지 않은 등급입니다.")

    print("-" * 50)

    cnt += 1
    total_money += user_amount
    

print("전체 주문 요약")

print(f"전체 주문 건 수 : {cnt}건")
print(f"총 구매 금액 : {total_money :,}원 | 총 할인 금액 : {total_discount :,}원 | 총 결제 금액 : {total_pay :,}원")
