num = ""

def get_grade(score):
    global num

    if score >= 90:
        num = "A"
    elif score >= 80:
        num = "B"
    elif score >= 70:
        num = "C"
    else:
        num = "F"
    return

score = int(input("점수를 입력하세요 : "))
get_grade(score)
print(f"학생의 학점은 {num}입니다.")