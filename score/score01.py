name = input("이름 : ")
kor = int(input("국어 : "))
eng = int(input("영어 : "))
math = int(input("수학 : "))

total = kor + eng + math
avg = total / 3

print("-" * 50)
print(f"이름 : {name}\n국어 : {kor}점\n영어 : {eng}점\n수학 : {math}점")
print("-" * 50)

print(f"총점 : {total}점")
print(f"평균 : {avg: .2f}점")

print("학점 : ")
if kor < 40 or eng < 40 or math < 40 :
    print("F")
elif avg >= 90 :
    print("A")
elif avg >= 80 :
    print("B")
elif avg >= 70 :
    print("C")
elif avg >= 60 :
    print("D")
else :
    print("F")

print("-" * 50)