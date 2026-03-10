num = int(input("측정 횟수 : "))

# 누적 값
cnt = 0
# 최대값
max = 0
# 최소값
min = 0

for i in range(1, num+1) :
    print(f"응답 시간 {i} (ms) ", end="")
    time = int(input(": "))

    if i == 1 :
        max = time
        min = time
    else :
        if time > max :
            max = time

        if time < min :
            min = time
    
    if time >= 0 and time <= 100 :
        print("FAST")
    elif time > 100 and time <= 300 :
        print("NORMAL")
    elif time > 300 and time <= 1000 :
        print("SLOW")
    elif time > 1000 :
        print("CRITICAL")

    cnt += time

print("-" * 40)

print(f"평균 응답 시간 : {cnt / num :.1f}ms")
print(f"최대 : {max}ms | 최소 : {min}ms")
