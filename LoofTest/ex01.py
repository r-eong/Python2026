#  code 의 값을 input 으로 입력받는다
code = int(input("상태코드를 입력하세요 : "))

# 다중if 사용
if code == 200 :
    print("상태 : 200 OK - 요청성공")
elif code == 201 :
    print("상태 : 201 Created - 리소스 생성 성공")
elif code == 400 :
    print("상태 : 400 Bad Request - 잘못된 요청")
elif code == 401 :
    print("상태 : 401 Unauthorized - 인증 필요")
elif code == 403 :
    print("상태 : 403 Forbidden - 접근 권한 없음")
elif code == 404 :
    print("상태 : 404 Not Found - 리소스 없음")
elif code == 201 :
    print("상태 : Internal Server Error - 서버 내부 오류")
else :
    print(f"{code} Unknown Status Code")

if code >= 200 and code <= 299 :
    print("계열 : 2XX - 성공")
elif code >= 400 and code <= 499 :
    print("계열 : 4XX - 클라이언트 오류")
elif code >= 500 and code <= 599 :
    print("계열 : 5XX - 서버오류")
