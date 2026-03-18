from datetime import date, datetime, timedelta

# 기준 날짜 (연체 확인용)
standardTodayStr = '2025-06-10'

# 도서 목록
books = [
    {'id':'B001','title':'파이썬 완전정복','author':'홍길동\t','genre':'IT','total':3,'available':3},
    {'id':'B002','title':'데이터분석 입문','author':'김데이터','genre':'IT','total':2,'available':2},
    {'id':'B003','title':'알고리즘의 이해','author':'이알고\t','genre':'IT','total':2,'available':1},
    {'id':'B004','title':'채식주의자','author':'한강\t','genre':'소설','total':4,'available':4},
    {'id':'B005','title':'82년생 김지영','author':'조남주\t','genre':'소설','total':3,'available':3},
]

# 대출 기록
loans = [
    {'loan_id':'L001','member':'박지수','book_id':'B003','loan_date':'2025-05-20','due_date':'2025-06-03','returned':False},
    {'loan_id':'L002','member':'최우진','book_id':'B001','loan_date':'2025-05-25','due_date':'2025-06-08','returned':False},
]

# 오늘 날짜
today = datetime.now()

# 14일 추가
after_14 = today + timedelta(days=14)

# 날짜 형식 변환
standardToday = datetime.strptime(standardTodayStr, "%Y-%m-%d")  # 기준 날짜
# today = datetime.strptime(today, "%Y-%m-%d")
formatToday = today.strftime('%Y-%m-%d')  # 오늘 날짜
formatAfter_14 = after_14.strftime('%Y-%m-%d')  # 14일 추가 날짜

# 도서 목록 조회
def show_books() :
    print(f"도서아이디\t제목\t\t\t저자\t\t장르\t수량\t상태")
    print("-" * 80)
    for b in books :
        print(f"{b['id']}\t\t{b['title']}\t\t{b['author']}\t{b['genre']}\t{b['available']}", end='\t')
        if b['available'] <= 0 :
            print("대출불가")
        else :
            print("대출가능")

# 도서 대출
def loan_book() :
    userName = input("회원명을 입력하세요 : ")
    bookingBoookId = input("대출 할 도서아이디를 입력하세요 : ")
    for b in books :
        print(bookingBoookId)
        print(b['id'])
        if b['id'] == bookingBoookId :  # 대출 할 도서 아이디가 존재하는지
            if b['available'] <= 0 :  # 그 아이디의 대출상태가 가능한지 (0권이하면 대여불가)
                print("[대출 실패] 대출이 불가능한 도서입니다.")
                
            else :  # 대출가능 - loans 리스트에 추가, avavilable -1, 대출번호 생성 (L001~)
                b['available'] -= 1  # 수량 -1
                print(f"[대출완료] {userName}님이 '{b['title']}'을(를) 대출하였습니다.")

                l_id = "L00" + str(len(loans)+1)

                loans.append({
                    'loan_id': l_id,
                    'member':userName,
                    'book_id': bookingBoookId,
                    'loan_date': formatToday,
                    'due_date': formatAfter_14,
                    'returned': False
                })

                print(f"대출 번호 : {l_id} | 반납 예정일 : {formatAfter_14}")
                # print(loans)
                
        else :
            print("존재하지 않는 도서입니다.")
            

# 도서 반납
def return_book() :
    returnBook = input("대출번호를 입력하세요 : ")

    for l in loans :
        if l['loan_id'] == returnBook :  # 반납 아이디 존재확인
            l['returned'] = True  # 반납상태 True 로 변경

            for b in books :
                if b['id'] == l['book_id'] :  # 반납 아이디의 대출 도서 아이디랑 도서 목록의 아이디 비교
                    print(f"[반납완료] '{b['title']}'이(가) 반납되었습니다.")
                    b['available'] += 1  # 도서 수량 +1
        elif l['returned'] == True :
            print("이미 반납된 도서입니다.")

# 대출 현황 조회
def show_loans() :

    print("대출번호\t회원명\t도서제목\t\t대출일\t\t반납예정일\t반납여부")
    print("-" * 88)

    for l in loans :
        for b in books :
            if l['book_id'] == b['id'] :
                print(f"{l['loan_id']}\t\t{l['member']}\t{b['title']}\t\t{l['loan_date']}\t{l['due_date']}\t", end='')
                if l['returned'] == False :
                    print("대출중")
                else :
                    print("반납완료")

# 연체 현황 조회
def show_overdue() :
    print(f"======================== 연체 현황 (기준일 : {standardTodayStr}) =======================")
    print("대출번호\t회원명\t도서제목\t\t반납예정일")
    print("-" * 80)

    for l in loans :
        for b in books :
            l_date = datetime.strptime(l['due_date'], "%Y-%m-%d")
            if l['book_id'] == b['id'] and l_date <= standardToday and l['returned'] == False :
                print(f"{l['loan_id']}\t\t{l['member']}\t{b['title']}\t\t{l['due_date']}")
                return

            else :
                print(f"{'현재 연체된 도서가 없습니다.' :^70}")
                return


# 장르별 조회
def show_genre_stats() :
    ITAllCnt = 0  # IT 전체 권수
    ITCnt  = 0  # IT 잔여 권수
    NovelAllCnt = 0  # 소설 전체권수
    NovelCnt = 0  # 소설 잔여 권수
    print("장르\t전체수량\t재고")
    print("-" * 30)

    for b in books :
        if b['genre'] == "IT" :
            ITAllCnt += b['total']  # 전체 권수
            ITCnt += b['available']  # 잔여 권수
        else :
            NovelAllCnt += b['total']  # 장르별 전체 권수
            NovelCnt += b['available']  # 잔여 권수
    print(f"IT\t{ITAllCnt}\t\t{ITCnt}")
    print(f"소설\t{NovelAllCnt}\t\t{NovelCnt}")

    
    


# -----------------------------------------------------------------------

while True :
    print("============================ 도서관 대출 관리 시스템 ===========================")
    print("1. 도서 목록 조회")
    print("2. 도서 대출")
    print("3. 도서 반납")
    print("4. 대출 현황 조회")
    print("5. 연체 현황 조회")
    print("6. 장르별 통계")
    print("0. 종료")

    menu = int(input("메뉴를 선택하세요 : "))
    print()

    # 도서 목록 조회
    if menu == 1 :
        show_books()
        print()

    # 도서 대출
    elif menu == 2 :
        loan_book()
        print()

    # 도서 반납
    elif menu == 3 :
        return_book()
        print()

    # 대출 현황 조회
    elif menu == 4 :
        show_loans()
        print()

    # 연체 현황 조회
    elif menu == 5 :
        show_overdue()
        print()

    # 장르변 조회
    elif menu == 6 :
        show_genre_stats()
        print()
        
    # 종료
    elif menu == 0 :
        print("종료되었습니다.")
        break

    else :
        print("존재하지 않는 메뉴입니다.")