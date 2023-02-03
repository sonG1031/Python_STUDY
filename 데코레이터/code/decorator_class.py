class Trace:
    def __init__(self, func): # 호출할 함수를 인스턴스의 초깃값으로 받음
        self.func = func

    def __call__(self):
        print(self.func.__name__, "function start")
        self.func()
        print(self.func.__name__, "function end")

@Trace # @데코레이터
def hello():
    print('hello')

hello()

