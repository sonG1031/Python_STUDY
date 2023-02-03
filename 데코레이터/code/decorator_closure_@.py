def trace(func):
    def wrapper():
        print(func.__name__, 'function start')
        func()
        print(func.__name__, 'function end')
    return wrapper

@trace
def hello():
    print('hello')

@trace
def world():
    print('world')


hello()
world()