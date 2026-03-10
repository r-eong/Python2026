# 다중 if문
# if 조건식 :
#    print("출력")
# elif 조건식 :
#    print("출력")
# else :
#    print("출력")

# 문제2
# 정수를 입력받아 0이면 0이다, 0보다 크면 양수이다. 아니면, 음수이다. 출력

num = int(input("정수를 입력하세요 : "))

if num == 0 :
    print("0임!")
elif num > 0 :
    print("양수임!")
else :
    print("음수임!")