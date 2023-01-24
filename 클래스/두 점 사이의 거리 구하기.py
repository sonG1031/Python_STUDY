# Date. 2023/01/18

# 클래스를 활용하여 2차원 평면에서 위치를 표현한 뒤 두 점 사이의 거리를 구하기
import math


class Point2D:
    def __init__(self, x, y) :
        self.x = x
        self.y = y

p1 = Point2D(x=30, y=20)
p2 = Point2D(x=60, y=50)

print(f'p1: {p1.x} {p1.y}')
print(f'p2: {p2.x} {p2.y}')


a = p2.x - p1.x
b = p2.y - p1.y

# math.sqrt() -> 제곱근을 반환함
c = math.sqrt((a**2) + (b**2))
print(c)


# [참고 | namedtuple 사용하기]
# 파이썬에서는 각 요소에 이름을 지정해 줄 수 있는 튜플인 namedtuple을 제공합니다( collections 모듈). 
# namedtuple은 자료형 이름과 요소의 이름을 지정하면 클래스를 생성해줍니다.
# 여기서 자료형 이름은 문자열, 요소의 이름은 문자열 리스트로 넣어줍니다.
# 클래스 = collections.namedtuple('자료형이름', ['요소이름1', '요소이름2'])
# namedtuple로 생성한 클래스는 값을 넣어서 인스턴스를 만들 수 있으며 
# 인스턴스.요소이름 
# 또는 
# 인스턴스[인덱스] 
# 형식으로 요소에 접근할 수 있습니다.