class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet

    def pay(self, amount):
        self.__wallet -= amount
        print(f'{self.__wallet} left now.')
minsub = Person('minsub', 17, 'seoul', 10000)
minsub.pay(3000)
# minsub.__wallet -= 1000 # Error, Because __wallet is private attribute.