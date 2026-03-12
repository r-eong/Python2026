# 함수 안에서 전역변수 사용하기
def cal_area(radius):
    global area
    area = 3.14 * radius ** 2
    return  # area 가 갖고 나가기 때문에 return 은 의미없음

area = 0  # 전역변수
r = float(input("반지름 입력 : "))
cal_area(r)
print(area)