class Duck:                 # 오리 클래스를 만들고 quack과 feathers 메서드 정의
    def quack(self): print('꽥~!')
    def feathers(self): print('오리는 흰색과 회색 털을 가지고 있습니다.')
 
class Person:               # 사람 클래스를 만들고 quack과 feathers 메서드 정의
    def quack(self): print('사람은 오리를 흉내냅니다. 꽥~!')
    def feathers(self): print('사람은 땅에서 깃털을 주워서 보여줍니다.')
 
def in_the_forest(duck):    # 덕 타이핑을 사용하는 함수. 클래스의 종류는 상관하지 않음
    duck.quack()            # quack 메서드와
    duck.feathers()         # feathers 메서드만 있으면 함수를 호출할 수 있음
 
donald = Duck()             # 오리 클래스로 donald 인스턴스를 만듦
james = Person()            # 사람 클래스로 james 인스턴스를 만듦
in_the_forest(donald)       # in_the_forest에 오리 클래스의 인스턴스 donald를 넣음
in_the_forest(james)        # in_the_forest에 사람 클래스의 인스턴스 james를 넣음