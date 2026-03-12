member_data = [
    {"name": "김철수", "age": 20},
    {"name": "이영희", "age": 25},
    {"name": "박민수", "age": 18}
]

adult_member = []

def filter_members():
    global adult_member

    for m in member_data:
        if m["age"] >= 20:
            adult_member.append(m["name"])

filter_members()

print(f"20세 이상 회원 : {adult_member}")
