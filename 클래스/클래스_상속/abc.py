from abc import *

class StudentBase(metaclass=ABCMeta):
    @abstractclassmethod
    def study(self):
        pass

    @abstractclassmethod
    def go_to_school(self):
        pass

class Student(StudentBase):
    def study(self):
        print('공부하기')

    def go_to_school(self):
        print('학교가기')
    

minsub = Student()
minsub.study() 
minsub.go_to_school()