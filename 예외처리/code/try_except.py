try:
    x = int(input('Enter the number to divide : '))
    y = 10 / x
    print(y)
except: # ZeroDivisionError
    print('예외가 발생했습니다.')