a, b = map(int, input().split())

for i in range(a, b+1):
    if i % 35 == 0: # 공배수일 때 'Fizz'나 'Buzz'가 출력되지 않도록 항상 공배수 처리를 먼저 해줍니다.
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Fizz')
    elif i % 7 == 0:
        print('Buzz')
    else:
        print(i)
