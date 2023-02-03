def trace(func):          # 호출할 함수를 매개변수로 받음
    def wrapper(*args, **kwargs):    # 가변 인수 함수로 만듦
        r = func(*args, **kwargs)    # func에 매개변수 args, kwargs를 넣어서 호출하고 반환값을 변수에 저장
        print('{0}(args={1},kwargs={2}) -> {3}'.format(func.__name__, args, kwargs, r))  # 매개변수와 반환값 출력
        return r          # func의 반환값을 반환
    return wrapper        # wrapper 함수 반환
 
@trace              # @데코레이터
def add(a, b):      # 매개변수는 두 개
    return a + b    # 매개변수 두 개를 더해서 반환
 
@trace
def get_max(*args):
    return max(args)

@trace
def get_min(**kwargs):
    return min(kwargs.values())

print(add(10, 20)) # trace는 위치 인수와 키워드 인수를 모두 처리할 수 있습니다. 따라서 가변 인수 함수뿐만 아니라 일반적인 함수에도 사용할 수 있습니다.
print(get_max(10, 20))
print(get_min(x=10, y=20, z=30))