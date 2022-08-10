for i in range(10, 0): # list(range(10, 0)) == []
    print('Hello world', i) # 실행안됨
# 왜냐하면 range는 숫자가 증가하는 기본 값이 양수 1이기 때문.

for i in range(10, 0, -1): # reversed함수를 통해 뒤집을수도 있음.
    print('Hello world', i)


dan = int(input())

for i in range(1, 10):
    print(f'{dan} * {i} = {dan * i}')

i = 2
j = 5
while i <= 32 or j > 0:
    print(i, j)
    i *= 2
    j -= 1

money = int(input())
money -= 1350
while money >= 0:
    print(money)
    money -= 1350
    