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

minsub = Student()
minsub.study() # error, go_to_school 메서드는 구현하지 않았으므로 에러가 발생합니다.

