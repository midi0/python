'''
class :  반복되는 불필요한 코드를 최소화하며 실 세계의 사물을 프로그래밍 상에서 쉽게 표현
하는 프로그래밍 기술

클래스의 요소
1.멤버: 내부에 포함되는 변수
2.함수: 내부에 포함되는 변수를 메소드라 칭함

인스턴스 : 클래스로 정의된 객체를 프로그램 상에서 이용가능하게 만든 변수

상속 : 다른 클래스의 멤버 변수와 메소드를 물려 받아 사용하는 기법
만약 자식과 부모클래스가 동일한 변수나 메소드를 가질 경우 자식 메소드를 먼저 처리한다

class Car:
    #클래스의 생성자
    def __init__(self, name, color):
        self.name = name #클래스의 멤버
        self.color = color #클래스의 멤버
    #클래스의 소멸자
    def __del__(self):
        print("인스턴스를 소멸시킵니다.")
    #클래스의 메소드
    def show_info(self):
        print("이름 :", self.name, "/ 색상 : ", self.color)
    #Setter 메소드
    def set_name(self, name):
        self.name = name

#인스턴스 생성
car1 = Car("소나타", "빨간색")
car1.show_info()
car1.set_name("쏘오나타")
print(car1.name, "를 구매했습니다.")
del car1#car1 인스턴스를 메모리에서 할당 해제시킨다.

car2 = Car("아반떼", "검은색")
car2.show_info()
'''

#부모 클래스 생성
class Unit:
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def attack(self):
        print(self.name, "이 공격합니다. [전투력 :", self.power,"]")
#자식 클래스 생성
class Monster(Unit):
    def __init__(self, name, power, type):
        self.name = name
        self.power = power
        self.type = type
    def show_info(self):
        print("몬스터 이름 : ",self.name, "/ 몬스터 종류 : ", self.type)

monster = Monster("슬라임", 10, "유체")
monster.attack()
monster.show_info()