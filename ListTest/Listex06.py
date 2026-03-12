# 메뉴 목록
role_menus = {
    'ADMIN' : ['대시보드', '회원관리', '상품관리', '주문관리', '통계', '시스템설정'],
    'MANAGER': ['대시보드', '상품관리', '주문관리', '통계'],
    'USER' : ['대시보드', '내정보', '주문내역'],
}
# 사용자 목록
users = [
    {'name': '관리자김', 'role': 'ADMIN'},
    {'name': '매니저박', 'role': 'MANAGER'},
    {'name': '일반이', 'role': 'USER'},
    {'name': '일반최', 'role': 'USER'},
]

# 관리자
ADMIN = {}
# 매니저
MANAGER = {}
# 일반 유저
USER = {}

for u in users:
    if u["role"] == "ADMIN":
        ADMIN["name"] = u["name"]
        ADMIN["role"] = u["role"]
    elif u["role"] == "MANAGER":
        MANAGER["name"] = u["name"]
        MANAGER["role"] = u["role"]
    else:
        USER["name"] = u["name"]
        USER["role"] = u["role"]

for r in role_menus:
    if r == "ADMIN":
        ADMIN["menu"] = role_menus[r]
    elif r == "MANAGER":
        MANAGER["menu"] = role_menus[r]
    else:
        USER["menu"] = role_menus[r]

# ------------------------------------------

print(f"{ADMIN["name"]} [{ADMIN["role"]}]")

for a in ADMIN["menu"]:
    print(f"- {a}")

# ------------------------------------------

print(f"{MANAGER["name"]} [{MANAGER["role"]}]")

for a in MANAGER["menu"]:
    print(f"- {a}")

# ------------------------------------------

print(f"{USER["name"]} [{USER["role"]}]")

for a in USER["menu"]:
    print(f"- {a}")
