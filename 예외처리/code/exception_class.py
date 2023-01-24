class NotThreeMultipleError(Exception):
    def __init__(self):
        super().__init__('3의 배수가 아님.')

def three_multiple():
    try:
        x = int(input('3의 배수를 입력하세요: '))
        if x % 3 != 0:
            raise NotThreeMultipleError
        print(x)
    except Exception as e:
        print(e)

three_multiple()