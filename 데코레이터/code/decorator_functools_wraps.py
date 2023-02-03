import functools
 
def is_multiple(x):
    def real_decorator(func):
        @functools.wraps(func)    # @functools.wraps에 func를 넣은 뒤 wrapper 함수 위에 지정
        def wrapper(a, b):
            r = func(a, b)
            if r % x == 0:
                print('{0}의 반환값은 {1}의 배수입니다.'.format(func.__name__, x))
            else:
                print('{0}의 반환값은 {1}의 배수가 아닙니다.'.format(func.__name__, x))
            return r
        return wrapper
    return real_decorator
 
@is_multiple(3)
@is_multiple(7)
def add(a, b):
    return a + b
 
add(10, 20)
# 함수의 원래 이름을 출력하고 싶다면 functools 모듈의 wraps 데코레이터를 사용