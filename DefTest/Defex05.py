menu = {"아메리카노": 3000, "라떼": 3500, "에이드": 4000}

def order_coffee(order, cnt = 1):
    # for m in menu.keys():
    if order in menu:
        print(f"{order} {cnt}잔 주문완료! | 총 금액 : {menu[order] :,}원")
        return
    else:
        print(f"죄송합니다. {order} 메뉴는 준비되어 있지 않습니다.")
        return

order_coffee("아메리카노")
order_coffee("라떼", 3)
order_coffee("에이드")