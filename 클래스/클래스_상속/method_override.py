class Person:
    def greeting(self):
        print('안녕하세요.')


class Student(Person):
    def greeting(self):
        print('안녕하세요. 저는 한양공고 학생입니다.')

minsub = Student()
minsub.greeting()