def calc():
    a = 3
    b = 5
    def mul_add(x):
        return a * x + b
    return mul_add

c = calc() # c에 저장된 함수가 클로저
print(c(1), c(2), c(3), c(4), c(5))


# lambda로 클로저 만들기

def lambda_calc():
    a = 3
    b = 5
    return lambda x : a * x + b

c = lambda_calc()
print(c(1), c(2), c(3), c(4), c(5))

# 클로저의 지역 변수 변경하기

def nonlocal_calc():
    a = 3
    b = 5
    total = 0
    def mul_add(x):
        nonlocal total
        total += a * x + b # a * x + b의 결과를 함수 calc의 지역 변수 total에 누적
        print(total)
    return mul_add


# 연습 문제 : 호출 횟수를 세는 함수 만들기
def counter():
    i = 0
    def count():
        nonlocal i
        i += 1
        return i
    return count
                       
c = counter()
for i in range(10):
    print(c(), end=' ')


# 심사 문제
def countdown(n):
    n += 1
    def down():
        nonlocal n
        n -= 1
        return n
    return down

n = int(input())
 
c = countdown(n)
for i in range(n):
    print(c(), end=' ')