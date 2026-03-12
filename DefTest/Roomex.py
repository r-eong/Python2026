# 객실 정보 : ID, 방이름, 가격, 최대인원, 현재상태 True/False
rooms = [
    {"id": 101, "roomName": "스탠다드 A", "price": 100000, "maxPeople": 2, "status": True},
    {"id": 102, "roomName": "스탠다드 B", "price": 110000, "maxPeople": 2, "status": True},
    {"id": 201, "roomName": "디럭스 룸", "price": 250000, "maxPeople": 4, "status": True},
    {"id": 301, "roomName": "스위트 룸", "price": 500000, "maxPeople": 6, "status": True},
]

total_price = 0
total_admin = 0

# 예약 내역
reservations = []

# 전체 객실 목록 : 매개변수가 True면 예약 가능한 방만, False면 전체를 보여줌
def show_rooms():
    print("=" * 67)
    print("ID\t객실명\t\t가격\t\t최대인원\t상태")
    print("-" * 67)
    for r in rooms:
        print(f"{r["id"]}\t{r["roomName"]}\t{r["price"] :,}\t\t{r["maxPeople"]}\t\t", end="")
        if r["status"] == True:
            print("예약 가능")
        else:
            print("예약 불가능")

    print("=" * 67)


# 해당 방이 예약 가능한지 확인 후, 가능하면 rooms의 상태를 변경하고 reservations 리스트에 예약 정보를 튜플로 추가
# input 으로 방 번호와 이름 받기
def make_reservation(room_id, guest_name, people, days):
    global reservations
    global total_price
    global total_admin

    for r in rooms:
        # 해당 방이 존재하는지, 예약 가능 상태인지 확인
        if r["id"] == room_id and r["status"] == True:

            # 최대 인원수 확인
            if r["maxPeople"] >= people:
                reservations.append((room_id, guest_name, people, days))
                r["status"] = False  # 예약 불가능으로 변경
                print(f"{guest_name}님 외 {people - 1}명 ({days}일), {room_id}호 예약이 완료되었습니다.")
                print(f"결제 금액 : {r["price"] * days:,}원")
                total_price += r["price"] * days
                total_admin += total_price

            else :
                reservations.append((room_id, guest_name, people, days))
                r["status"] = False  # 예약 불가능으로 변경
                addPrice = (((people - r["maxPeople"]) * 20000 ) + r["price"]) * days
                total_price += addPrice
                total_admin += total_price
                print(f"{guest_name}님 외 {people - 1}명 ({days}일), {room_id}호 예약이 완료되었습니다.")
                print(f"결제 금액 : {addPrice:,}원")

        # else:
        #     print("존재하지 않거나 예약 불가능한 객실입니다. 확인 후 다시 입력해주세요.")
        #     break

def max_people(room_id):

    for r in rooms:
        if r["id"] == room_id:
            peo = r["maxPeople"]

    return peo

# 방 ID와 숙박일수, 인원수를 입력받아 총액을 계산하여 반환
def calculate_price():

    print("-------------------------- 전체 예약 명단 -------------------------")
    for r in reservations :
        print(f"성함 : {r[1]} | 객실 번호 : {r[0]} | 인원 : {r[2]} | 투숙 일수 : {r[3]} | 결제 금액 : {total_price :,}원")

    print(f"전체 매출 : {total_admin :,}원")
# 예약 목록에서 해당 방의 예약을 삭제하고 객실상태를 다시 True(가능)로 변경
# def cancel_reservation(res_list, room_id):

while True:
    print("--------------------- 리조트 예약 관리 시스템 ---------------------")
    print("1. 객실 현황 보기")
    print("2. 객실 예약하기")
    print("3. 예약 내역 및 매출 확인")
    print("4. 프로그램 종료")
    menu = int(input("원하는 메뉴를 선택하세요 : "))

    # 객실 현황 보기
    if menu == 1 :
        show_rooms()  # 전체 객실 목록

    # 객실 예약하기
    elif menu == 2:
        show_rooms()  # 전체 객실 목록

        room_id = int(input("예약하실 객실 ID를 입력하세요 : "))

        peo = max_people(room_id)
        people = int(input(f"투숙 인원을 입력하세요 (최대 {peo}명) : "))
        days = int(input("투숙 기간을 입력하세요 : "))
        guest_name = input("예약자 성함을 입력하세요 : ")

        make_reservation(room_id, guest_name, people, days)

        print()
        
    # 예약 내역 및 매출 확인
    elif menu == 3:
        calculate_price()

    # 프로그램 종료
    elif menu == 4:
        print("프로그램을 종료합니다.")
        break
    else :
        print("없는 메뉴입니다.")
        continue