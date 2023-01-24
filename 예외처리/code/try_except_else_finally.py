try:
    x = int(input('Enter the number to divide : '))
    y = 10 / x
except ZeroDivisionError:
    print('cannot divide the number to 0.')
else:
    print(y)
finally:
    print('code running is done.')