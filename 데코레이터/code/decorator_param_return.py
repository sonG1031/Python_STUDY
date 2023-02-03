def trace(func):          # 호출할 함수를 매개변수로 받음
    def wrapper(a, b):    # 호출할 함수 add(a, b)의 매개변수와 똑같이 지정
        r = func(a, b)    # func에 매개변수 a, b를 넣어서 호출하고 반환값을 변수에 저장
        print('{0}(a={1}, b={2}) -> {3}'.format(func.__name__, a, b, r))  # 매개변수와 반환값 출력
        return r          # func의 반환값을 반환
    return wrapper        # wrapper 함수 반환
 
@trace              # @데코레이터
def add(a, b):      # 매개변수는 두 개
    return a + b    # 매개변수 두 개를 더해서 반환
 
print(add(10, 20))


# 매개변수와 반환값을 처리하는 데코레이터를 만들 때는 먼저 안쪽 wrapper 함수의 매개변수를 호출할 함수 add(a, b)의 매개변수와 똑같이 만들어줍니다.
# func에는 매개변수 a와 b를 그대로 넣어줍니다. 
# wrapper 함수에서 func의 반환값을 출력할 필요가 없으면 return func(a, b)처럼 func를 호출하면서 바로 반환해도 됩니다.