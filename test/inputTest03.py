name = input("이름을 입력하세요 : ")
height = float(input("키를 입력하세요(cm) : "))
kg = float(input("체중을 입력하세요(kg) : "))

pyojunKG = (height - 100) * 0.9
bibandoo = kg / pyojunKG * 100

print("-" * 50)
print(f"{name}님의 비만도는 {bibandoo: .2f}% 입니다.")
print("-" * 50)