class Person:
    count = 0 # 클래스 속서

    def __init__(self):
        Person.count += 1

    @classmethod
    def print_count(cls):
        print(f'{cls.count}명 생성됨.')


minsub = Person()
kim = Person()

Person.print_count()
minsub.print_count() # 클래스 속성, 메서드를 찾는 과정에서 인스턴스 메서드가 아니면 클래스 메서드를 호출함.