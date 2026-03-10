num1 = int(input("첫 번째 숫자를 입력하세요 : "))
num2 = int(input("두 번째 숫자를 입력하세요 : "))

print("-" * 50)

plus = num1 + num2
minus = num1 - num2
gop = num1 * num2
na = num1 / num2

print(f"{num1}{" + "}{num2}{" = "}{plus}")
print(f"{num1}{" - "}{num2}{" = "}{minus}")
print(f"{num1}{" * "}{num2}{" = "}{gop}")
print(f"{num1}{" / "}{num2}{" = "}{na}")