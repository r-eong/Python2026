# 문제
# 년도가 4로 나누어 떨어지면 윤년
# 100으로 나누어 떨어지면 제외
# 400으로 나누어 떨어지면 윤년

year = int(input("년도를 입력하세요 : "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
    print("윤년임!")
else :
    print("윤년아님!")