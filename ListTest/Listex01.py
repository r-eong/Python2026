products = ['노트북', '마우스', '키보드', '모니터', '웹캠']
stocks = [15, 3, 8, 22, 5]

stoTotal = 0

print("=== 재고 현황 ===")

for i in range(0, len(products)) :
    print(products[i], ": ", stocks[i], "개", end=" ")
    stoTotal += stocks[i]

    if stocks[i] < 10 :
        print("재고 부족")
        print()

print("전체 재고 합계 : ", stoTotal, "개")

# for i in range(0, len(products)) :
#     product = products[i]
#     stock = stocks[i]
#     # 파이썬은 문자와 숫자를 하나로 나열할 수 없다. 
#     # 그러므로 str 함수를 이용해 숫자를 문자로 변환하여 나열한다.
#     msg = product + " : " + str(stock) + "개"
#     if stock < 10 :
#         msg = msg + " 재고 부족"
#     print(msg)

# total = 0
# for st in stocks :
#     total += st

# print(f"전체 재고 합계 : {total}개")