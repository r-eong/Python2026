# 파이썬의 함수는 return 값을 여러개 받을 때 튜플을 사용한다.
def cal(a, b):
    sum = a + b
    diff = a - b

    return sum, diff  # <- 튜플로 묶어서 반환
s, d = cal(10, 5)

print(f"합 : {s} / 차 : {d}")