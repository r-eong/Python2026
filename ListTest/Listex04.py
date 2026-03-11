response = {
    'code' : 200,
    'message': 'success',
    'data' : [
        {'userId': 'user01', 'name': '이자바', 'score': 95},
        {'userId': 'user02', 'name': '박리액트', 'score': 82},
        {'userId': 'user03', 'name': '최스프링', 'score': 91},
        {'userId': 'user04', 'name': '정마이바티스', 'score': 78},
    ]
}

print("===== 전체 성적 =====")

res_data = response['data']

for r in res_data :
    if response['code'] == 200 :
        print(f"{r['name']} ({(r['userId'])}) : {r['score']}점")

print()

# goob_student = {}

# for r in res_data :
#     if r['score'] >= 90 :
#         goob_student['name'] = r['name']
#         goob_student['score'] = r['score']
#         print(goob_student)

goob_student = []

for r in res_data :
    if r['score'] >= 90 :
        goob_student.append({"name" : r['name'], "score": r['score']})
        print(goob_student)

print(f"===== 우수 수강생 (90점 이상) {len(goob_student)}명 =====")
for g in goob_student :
    print(f"{g['name']} : {g['score']}점")