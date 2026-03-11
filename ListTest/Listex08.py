student = [
    {"subject": "Python 프로그래밍", "score": 92, "credit": 3},
    {"subject": "Spring Boot 개발", "score": 88, "credit": 3},
    {"subject": "React 프론트앤드", "score": 76, "credit": 2},
    {"subject": "데이터베이스\t", "score": 95, "credit": 3},
    {"subject": "알고리즘\t", "score": 68, "credit": 2},
]

# 총 학점포인트
total_score = 0
# 총 이수학점
total_credit = 0
# 총 GPA
total_gpa = 0

# 학점 분포
dis = {"A+": 0, "A": 0, "B+": 0, "B": 0, "C+": 0, "C": 0, "D": 0, "F": 0}

print("============================= 성적표 ============================")
print("과목\t\t\t점수\t학점\t학점포인트\t이수학점")
print("-" * 65)

# 학점, 학점 포인트 계산
for s in student :
    if 95 <= s["score"] :
        s["unit"] = "A+"
        s["unit_point"] = 4.5
        dis["A+"] += 1
    elif 90 <= s["score"] < 95 :
        s["unit"] = "A"
        s["unit_point"] = 4.0
        dis["A"] += 1
    elif 85 <= s["score"] < 90 :
        s["unit"] = "B+"
        s["unit_point"] = 3.5
        dis["B+"] += 1
    elif 80 <= s["score"] < 85 :
        s["unit"] = "B"
        s["unit_point"] = 3.0
        dis["B"] += 1
    elif 75 <= s["score"] < 80 :
        s["unit"] = "C+"
        s["unit_point"] = 2.5
        dis["C+"] += 1
    elif 70 <= s["score"] < 75 :
        s["unit"] = "C"
        s["unit_point"] = 2.0
        dis["C"] += 1
    elif 65 <= s["score"] < 70 :
        s["unit"] = "D"
        s["unit_point"] = 1.0
        dis["D"] += 1
    else :
        s["unit"] = "F"
        s["unit_point"] = 0.0
        dis["F"] += 1

    # 총 이수학점
    total_credit += s["credit"]
    # 총 학점포인트
    total_score += s["score"]
    # GPA = 모든 과목의 (학점포인트 * 이수학점) 총합 / 총 이수학점
    gpa = s["unit_point"] * s["credit"]
    total_gpa += gpa

    print(f"{s["subject"]}\t{s["score"]}점\t{s["unit"]}\t{s["unit_point"]}\t\t{s["credit"]}학점")

print()

print(f"GPA : {total_gpa/total_credit :.2f} / 4.50 (총 {total_credit}학점)")
print(f"학점 분포 - A+ : {dis['A+']}, A : {dis['A']}, B+ : {dis['B+']}, B : {dis['B']}, C+ : {dis['C+']}, C : {dis['C']}, D : {dis['D']}, F : {dis['F']}")