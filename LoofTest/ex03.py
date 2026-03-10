SELECT = 0
INSERT = 0
UPDATE = 0
DELETE = 0

while True :
    # upper : input 에서 소문자로 입력받아도 대문자로 출력되는 함수 
    # lower : 이건 무조건 소문자
    qu = input("쿼리 유형 입력 : ").upper()

    if qu == "SELECT" :
        SELECT += 1
    elif qu == "INSERT" :
        INSERT += 1
    elif qu == "UPDATE" :
        UPDATE += 1
    elif qu == "DELETE" :
        DELETE += 1
    elif qu == "EXIT" :
        break
    else :
        print("알 수 없는 쿼리유형 입니다.")

print("--- 쿼리 실행 현황 ---")
print(f"SELECT : {SELECT}회")
print(f"INSERT : {INSERT}회")
print(f"UPDATE : {UPDATE}회")
print(f"DELETE : {DELETE}회")
print(f"총 실행 : {SELECT + INSERT + UPDATE + DELETE}회")

if SELECT / (SELECT + INSERT + UPDATE + DELETE) >= 0.7 :
    print("SELECT 쿼리 비중이 높습니다. 캐싱을 고려하세요.")