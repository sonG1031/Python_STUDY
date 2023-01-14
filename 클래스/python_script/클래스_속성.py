class Person:
    '''사람 클래스입니다.'''
    # 클래스 속성
    bag = []

    def put_bag(self, stuff):
        '''가방에 넣기 메서드입니다.'''
        # self는 현재 인스턴스를 뜻하므로 클래스 속성을 지칭하기에는 조금 모호
        # self.bag.append(stuff)
        Person.bag.append(stuff)

minsub = Person()
minsub.put_bag('책')

kim = Person()
kim.put_bag('열쇠')

print(minsub.bag) # minsub.__dict__['bag']
print(kim.bag)

print(minsub.__dict__) 
print(Person.__dict__)

print(Person.__doc__)
print(Person.put_bag.__doc__)
