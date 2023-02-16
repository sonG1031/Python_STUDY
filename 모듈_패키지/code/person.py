class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    def greeting(self):
        print(f'Hi. I am {self.name}.')

        