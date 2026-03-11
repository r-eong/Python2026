# 리스트 = 배열과 같은 역할
# 리스트 [숫자, 문자, 혼합] 사용 가능
# 동적 => 길이 고정 X
# 속도는 조금 느림

heroes = []

# 01. 리스트 추가하는 방법

# - append('추가할 문자') => 맨 뒤에 추가
heroes.append('아이어맨')
heroes.append('닥터 스트레인지')
# - insert(인덱스번호, '추가할 문자') => 인덱스 번호에 추가
heroes.insert(1,'왕과 사는 남자')

print(heroes[2])

# ------------------------------------------------------------------------

# 02. 리스트 삭제하는 방법

# - remove('삭제할 문자')
heroes.remove('왕과 사는 남자')
# - del heroes[0] => 0번째 데이터 삭제
del heroes[1] 
# - pop => 마지막 데이터 삭제
heroes.pop()

print(heroes)

# ------------------------------------------------------------------------

heroes.append('a')
heroes.append('b')
heroes.append('c')
heroes.append('d')
print(heroes)

# for문 이용해서 출력
for title in heroes:
    print(title,end=" ") # end=" " -> 가로로 출력

print()

# 리스트 슬라이스
# heroes[0:3] => 0번째부터 3글자
# heroes[:3] => 처음부터 3글자
# heroes[3:] => 3번째부터 마지막까지

# cut = heroes[0:2] # ['a', 'b']
# cut = heroes[:3] # ['a', 'b', 'c']

# hores[0:3] : 0번째 부터 3글자
# hores[:3] : 처음부터 3글자
# hores[0:] : 세번째 글자부터 마지막까지
cut = heroes[0:2]
print(cut)

# 문제)
# movieTitle = [] 에 아래 제목 4개를 추가하시오
# 아이언맨, 토르, 헐크, 스칼렛 위치
movieTitle = []
movieTitle.append("아이언맨")
movieTitle.append("토르")
movieTitle.append("헐크")
movieTitle.append("스칼렛 위치")

# print(movieTitle)
for movie in movieTitle :
    print(movie, end=" ")

print()

# 문제)
# movieTitle 에 '토르'가 존재하면 삭제하고 출력
if "토르" in movieTitle :
    movieTitle.remove("토르")

movieTitle.sort(reverse=True)

for movie in movieTitle :
    print(movie, end=" ")