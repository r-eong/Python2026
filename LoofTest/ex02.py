# 아이디
while True :
    id = input("아이디를 입력하세요 (4~12자) : ")

    if len(id) >= 4 and len(id) <= 12 :
        break
    print("아이디는 4자 이상, 12자 이하여야 합니다. 다시 입력하세요.")

# 비밀번호
while True :
    pw = input("비밀번호를 입력하세요 (8자 이상, 숫자 포함) : ")

    if len(pw) < 8 :
        print("비밀번호는 8자 이상이어야 합니다. 다시 입력하세요.")
        continue  # 아래 코드를 실행하지 않고 다시 입력

    # 숫자 포함되어 있는지 존재 유무를 확인하는 boolean
    found = False

    # in
    # if @ in 변수 : @가 변수 안에 포함되어 있는지
    # for i in 변수 : i 값이 변수까지 반복해준다
    for pwChk in pw :
        # 문자가 0 이상이고 9 이하이면 숫자
        if pwChk >= "0" and pwChk <= "9" :
            found = True  # 숫자가 포함되어 있음
            break  # for문 종료
        
    # 숫자가 하나도 없으면 다시 입력
    if not found : 
        print("비밀번호는 숫자가 포함되어 있어야 합니다. 다시 입력하세요.")
        continue

    # 모든 조건을 만족하면 반복문 종료
    break

# 이메일
while True :
    email = input("이메일을 입력하세요. ex) example@mail.com : ")

    if "@" in email :
        break
    print("올바른 이메일 형식이 아닙니다. 다시 입력하세요.")

print("유효성 검사 통과! API 요청을 전송합니다.")