# 튜플이란?
# 여러개의 데이터를 순서대로 저장
# 단, 수정/삭제/추가 안됨
# 예) a = (10, 20, 30)
# 접근 방법 : a[0]

a = (10, 20, 30)
# a[0] = 15  <- 수정 불가능
print(a[0])

# --------------------------------------------

fruit = ("apple", "banana", "orange")

for f in fruit :
    # print(f)
    print(f, end=" ")

print()

if "abcd" in fruit :
    print("O")
else :
    print("X")

# --------------------------------------------

# 튜플은 괄호가 없어도 됨
t =  10, 20, 30
print(t)

# --------------------------------------------

# 문제
# 주어진 자료를 이용해 합계, 평균을 구하시오
score = (80, 50, 75, 90)
total = 0
avg = 0

for s in score :
    total += s
    avg = total / len(score)

print(f"합계 : {total} / 평균 : {avg}")