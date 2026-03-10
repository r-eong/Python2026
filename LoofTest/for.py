# for문에서 range 는 0 ~ n-1 까지 반복된다
# for i in range(5):
#     print("방문을 환영합니다.")

# ------------------------------------------

# 1부터 5까지 출력
# n = 5
# for i in range(1, 20, n-1):
#     print(i)

# ------------------------------------------

#  5! = 1 * 2 * 3 * 4 * 5 = 120
# n = int(input("정수를 입력하세요 : "))
# fact = 1
# for i in range(1, n+1):
#     fact = fact * i

# print(f"{n}!은 {fact}이다.")

# ------------------------------------------

for i in range(2, 9):
    for j in range(1, 9):
        print(f"{i} * {j} = {i*j}")
    print()