class Person:
    pass
class Bird:
    pass
class Student(Person):
    pass
p, s = Person(), Student()

print("p is instance of Person: ", isinstance(p, Person))
# s는 Person을 상속받았으니
print("s is instance of Person: ", isinstance(s, Person))
# 모든 class의 root는 object
print("p is instance of Object: ", isinstance(p, object))
print("p is instance of Bird: ", isinstance(p, Bird))
print("int is instance of Object: ", isinstance(int, object))