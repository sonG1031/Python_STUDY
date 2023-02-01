def sum_coroutine():
    try:
        total = 0
        while True:
            x = (yield total) 
            total += x
    except RuntimeError as e:
        print(e)
        yield total


co = sum_coroutine()
next(co)

for i in range(20):
    co.send(i)

print(co.throw(RuntimeError, '예외로 코루틴 끝내기'))

# 코루틴 바깥에서는 co.throw(RuntimeError, '예외로 코루틴 끝내기')와 같이 
# throw 메서드에 RuntimeError 예외와 에러 메시지를 지정하면 코루틴 안에서 예외가 발생합니다. 
# 그리고 코루틴 안의 except에서 yield를 사용하여 바깥으로 전달한 값은 throw 메서드의 반환값으로 나옵니다
# 여기서는 코루틴 안에서 예외 처리를 했으므로 '예외로 코루틴 끝내기'가 출력되고, 코루틴 바깥에서는 누적된 값 190이 출력됩니다.