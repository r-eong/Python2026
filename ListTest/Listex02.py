member = {
    'name' : '김파이썬',
    'email' : 'python@example.com',
    'age': 28,
    'grade' : 'GOLD'
}

print("=== 회원 정보 ===")

for user in member :
    print(f"{user} : {member[user]}")

    if 0 <= member['age'] < 20 :
        ageChk = "주니어"
    elif 20 <= member['age'] <= 39 :
        ageChk = "일반"
    else :
        ageChk = "시니어"

    if user == "phone" :
        phoneChk = member['phone']
    else :
        phoneChk = "미등록"

print()
print(f"연령 구간 : {ageChk}")
print(f"연락처 : {phoneChk}")

