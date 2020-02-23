class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def say_hello(self, to_name):
        print("안녕 " + to_name + ", 내 이름은 " + self.name)

    def introduce(self):
        print("내 이름은 " + self.name + "이고 나이는 " + str(self.age) + "살 이야")
    
class Police(Person): #Person을 상속받는다는 뜻
    def arrest(self, to_arrest):
        print("넌 체포됐다, " + to_arrest)

class Programmer(Person):
    def program(self, to_program):
        print("다음에 만들 프로그램은 " + to_program)


seyoung = Person("세영", 26)
seyoung.say_hello("제니")
seyoung.introduce()

jenny = Police("제니", 24)
jenny.arrest("마이클")

michael = Programmer("마이클", 22)
michael.program("이메일 클라이언트")



