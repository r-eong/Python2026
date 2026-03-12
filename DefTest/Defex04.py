nums = [15, 3, 24, 8, 42, 10]
min = nums[0]
max = 0

def find_min_max():
    global min, max

    for n in nums:
        if n > max :
            max = n

        if n < min :
            min = n

find_min_max()

print(f"최대값 : {max} / 최소값 : {min}")