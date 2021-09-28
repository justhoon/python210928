# class1.py

# 클래스를 정의(새로운 형식 만들기)
class Person:
    #생성자(초기화) 메서드
    def __init__(self):
        self.name = "default name"

    def print(self):
        print("my name is {0}".format(self.name))

# 인스턴스 생성
p1 = Person()
p1.print()

