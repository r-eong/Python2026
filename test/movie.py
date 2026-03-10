# 데이터
cinema_name = "PYTHON CINEMA"
tiket_num = "2026-0309-01"
screening_room = "7관 (4층)"
movie_name = "파이썬의 습격"
screentime = "14:30 ~ 16:10"

adult = 15000
baby = 10000

# 계산
people_a = 2
people_b = 1

people_a_total = people_a * adult
people_b_total = people_b * baby

total = people_a_total + people_b_total

# 출력
print("=" * 60)
print(f"{cinema_name : ^60}")
print("=" * 60)

print(f"티켓번호 : {tiket_num}")
print(f"상영관 : {screening_room}")
print(f"영화명 : {movie_name}")
print(f"상영시간 : {screentime}")

print("-" * 60)
print(f"{"구분"}{"단가": >28}{"인원": >10}{"금액": >10}")
print("-" * 60)

print(f"{"성인"}{adult : >30,}{people_a : >11}{people_a_total : >13,}")
print(f"{"청소년"}{baby : >28,}{people_b : >11}{people_b_total : >13,}")
print("-" * 60)

print(f"{"총 금액"}{total : >51,}")
print("=" * 60)