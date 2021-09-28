# class2.py

# 클래스를 정의(새로운 형식 만들기)
class Person:
    num_person = 0
    #생성자(초기화) 메서드
    def __init__(self):
        self.name = "default name"
        Person.num_person += 1

    def print(self):
        print("my name is {0}".format(self.name))

# 인스턴스 생성
# 동기화테스트1
p1 = Person()
p2 = Person()
p3 = Person()
print("인스턴스의 갯수:{0}".format(Person.num_person))