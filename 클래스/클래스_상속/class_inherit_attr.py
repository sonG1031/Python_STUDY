class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = 'hello'


class Student(Person):
    def __init__(self):
        print('Student __init__')
        super().__init__() # 자바처럼 자동으로 부모 클래스를 초기화해주지 않음.
        # super(Student, self).__init__()
        self.school = 'hanyang tech highschool'

minsub = Student()
print(minsub.school)
print(minsub.hello)