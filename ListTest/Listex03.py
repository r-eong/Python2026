orders = [
    {'id': 1, 'product': '노트북', 'amount': 1200000, 'status': 'PAID'},
    {'id': 2, 'product': '마우스', 'amount': 35000, 'status': 'PENDING'},
    {'id': 3, 'product': '모니터', 'amount': 450000, 'status': 'PAID'},
    {'id': 4, 'product': '키보드', 'amount': 89000, 'status': 'CANCELLED'},
    {'id': 5, 'product': '웹캠', 'amount': 75000, 'status': 'PAID'},
]
# 결제 상품
paid = []
# 총 결제금액
total = 0

print("=== 결제 완료 주문 ===")
for order in orders :

    if order['status'] == "PAID" :
        paid.append(order)

for p in paid :
    print(f"{p['id']}번 주문 - 상품 : {p['product']} / 금액 : {p['amount'] :,}원")
    total += p['amount']

print(f"총 결제 금액 : {total :,}원")

# -------------- 풀이 --------------

# cart = []
# # for 작명 in 리스트
# # o 에는 orders 의 인덱스 첫 번째 값부터 순서대로 담긴다.
# # 고로 현재는 {'id': 1, 'product': '노트북', 'amount': 1200000, 'status': 'PAID'}, 를 읽어냄
# for o in orders :
#     # 딕셔너리는 반드시 key 값은 읽어야 value 를 출력할 수 있다.
#     if o['status'] == 'PAID' :
#         # paid 리스트에 append 로 상품을 추가함
#         cart.append(o)

# print("=== 결제 완료 주문 ===")

# cart_total = 0
# for c in cart :
#     print(f"{c['id']}번 주문 - 상품 : {c['product']} / 금액 : {c['amount'] :,}원")
#     # 총 금액 계산
#     cart_total += c['amount']

# print(f"총 결제 금액 : {cart_total :,}원")