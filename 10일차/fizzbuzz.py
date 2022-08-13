# 1부터 100까지 숫자를 출력하면서 3의 배수는 숫자 대신 'Fizz', 
# 5의 배수는 숫자 대신 'Buzz', 3과 5의 공배수는 숫자 대신 'FizzBuzz'를 출력하는 문제

for i in range(1, 101):
    # i % 3 == 0 and i % 5 == 0
    if i % 15 == 0: # 3과 5의 최소공배수
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

# i가 30인데 if에서 3의 배수를 먼저 검사하면 3과 5의 공배수는 검사를 하지 않고 
# 그냥 넘어가버리므로 주의해야 합니다. 따라서 3과 5의 공배수를 먼저 검사한 뒤 
# elif로 3의 배수, 5의 배수를 검사해야 합니다.

for i in range(1, 101):
    print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)
    # 3의 배수이면 'Fizz' * (i % 3 == 0) -> 'Fizz'
    # 5의 배수이면 'Fizz' * (i % 5 == 0) -> 'Buzz'
    # 3과 5의 공배수이면 'Fizz' + 'Buzz' -> 'FizzBuzz'
    # 다 아니면 '' or i -> i

# 이처럼 파이썬에서 연산자의 특성을 활용하면 코드의 길이를 짧게 줄일 수 있습니다. 