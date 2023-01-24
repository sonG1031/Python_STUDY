try:
    x = int(input('Enter the multiple of 3 : '))
    if x % 3 != 0:
        raise Exception('is not multiple of 3.')
except Exception as e:
    print('예외가 발생함.', e)