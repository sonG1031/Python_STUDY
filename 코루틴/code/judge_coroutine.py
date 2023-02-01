# 표준 입력으로 사칙연산 계산식이 여러 개 입력됩니다. 
# 다음 소스 코드에서 각 계산식의 결과를 구하는 코루틴을 만드세요. 
# 계산식은 문자열 형태이며 값과 연산자는 공백으로 구분됩니다. 
# 그리고 값은 정수로 변환하여 사용하고, 나눗셈은 / 연산자를 사용하세요.

def calc():
    result = None
    while True:
        e = (yield result).split()
        if e[1] == '+':
            result = int(e[0]) + int(e[2])
        elif e[1] == '-':
            result = int(e[0]) - int(e[2])
        elif e[1] == '*':
            result = int(e[0]) * int(e[2])
        elif e[1] == '/':
            result = int(e[0]) / int(e[2])



expressions = input().split(', ') # 1 + 2, 4 - 9
 
c = calc()
next(c)
 
for e in expressions:
    print(c.send(e))
 
c.close()