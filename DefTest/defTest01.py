# 파이썬 함수의 특징
# 함수 생성시 반드시 def 로 시작한다
# 함수를 실행할 떄는 함수 이름을 호출한다
# 매개변수 값을 전달할 때 함수이름(매개값)으로 한디
# 파이썬은 비역변수를 블록(for, if)등이 아니라 함수 (def) 기준으로 스코프(scope)가 나뉜다

# 스코프란?
# 변수를 사용할 수 있는 범위를 말한다
# 전역변수를 함수(def)안에서 사용하려면 반드시 global 명령어를 사용한다
# 함수에서 값을 return 받을 때 여러개인 경우 튜플을 이용한다
# 예) def test() ~ return (a, b)

def print_address():
    print("종로구")
    print("파이썬")
    print("홍길동")

# 반드시 함수 호출
print_address()

print()

# 함수에 매개변수 사용하기
def print_address01(name):
    print("종로구")
    print("파이썬")
    print(name)

print_address01("개나리")

print()

# 함수 값 반환하기
def cal_area(radius):
    area = 3.14 * radius ** 2
    return area

# 지역변수인 area 를 전역변수로 사용할 수 없다.
# print(area) # -> 오류
cal = cal_area(5)
print(cal)

print()

# 함수에 매개변수값 여러개 전달하기
def get_sum(start, end):
    sum = 0
    for i in range(start, end+1):
        sum += i
    return sum

print(get_sum(1, 10))

print()

# 함수의 매개변수를 input 으로 입력받아 결과값 출력
def cal_area02(radius):
    result = 3.14 * radius ** 2
    return result

num = float(input("입력하세요 : "))
print(cal_area02(num))