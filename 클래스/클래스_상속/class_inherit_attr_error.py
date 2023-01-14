class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = 'hello'


class Student(Person):
    def __init__(self):
        print('Student __init__')
        self.school = 'hanyang tech highschool'

minsub = Student()
print(minsub.school)
print(minsub.hello) # error, Person의 __init__ 메서드가 호출되지 않았기 때문.