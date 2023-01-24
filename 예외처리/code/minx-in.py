class HelloMixIn:
    def greeting(self):               # 인사하는 메서드는 공통적인 메서드
        print('안녕하세요.')
 
class Person():
    def __init__(self, name):
        self.name = name
 
class Student(HelloMixIn, Person):    # HelloMixIn과 Person을 상속받아 학생 클래스를 만듦
    def study(self):
        print('공부하기')
 
class Teacher(HelloMixIn, Person):    # HelloMixIn과 Person을 상속받아 선생님 클래스를 만듦
    def teach(self):
        print('가르치기')