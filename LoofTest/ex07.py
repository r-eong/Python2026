# 강도 확인 누적
cnt = 0
# 조건 만족
ok = "✓"
# 조건 불만족
none = "x"

length = none
big = none
smail = none
num = none
special = none

pw = input("비밀번호 입력 : ")

# 비밀번호 검사 
if len(pw) >= 8 :
    length = ok
    length_chk = True
    print(length, "length")

for ch in pw :
    if ch >= 'A' and ch <= 'Z' :
        big = ok
        big_chk = True
        print(big, "big")
    elif ch >= "a" and ch <= "z" :
        smail = ok
        smail_chk = True
        print(smail, "smail")
    elif ch >= "0" and ch <= "9" :
        num = ok
        num_chk = True
        print(num, "num")
    else :
        special = ok
        special_chk = True
        print(special, "special")

print(f"[{length}] 길이 8자 이상")
print(f"[{big}] 대문자 포함")
print(f"[{smail}] 소문자 포함")
print(f"[{num}] 숫자 포함")
print(f"[{special}] 특수문자 포함")
print("-" * 30)

# 비밀번호 강도 체크
if length_chk == True and big_chk == True and smail_chk == True and num_chk == True and special_chk == True :
    print("비밀번호 강도 : 매우 강함")
else :
    print("비밀번호 강도 : 취약")