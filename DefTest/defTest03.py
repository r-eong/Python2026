# defult 매개변수 지정하기
# 파이썬은 매개변수에 기본값을 지정할 수 있다. 
# 이것을 defult argument 라 한다.
def greet(name, msg="별일없죠"):
    print(f"안녕 {name} {msg}")

greet("개나리", "별일있죠")