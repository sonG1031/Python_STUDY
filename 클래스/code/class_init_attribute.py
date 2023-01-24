class Person:
    def __init__(self, name, age, address):
        self.hello = 'hello!'
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print(f'{self.hello} Im {self.name}.')

minsub = Person('minsub', 17, 'seoul')
minsub.greeting()

print('name : ', minsub.name)
print('age : ', minsub.age)
print('address : ', minsub.address)