class Person:
    def greeting(self):
        print('안녕하세요.')

class University:
    def manage_credit(self):
        print('학점 관리')

class Undergraduate(Person, University):
    def study(self):
        print('공부하기')

minsub = Undergraduate()
minsub.greeting()
minsub.manage_credit()
minsub.study()