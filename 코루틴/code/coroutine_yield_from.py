def accumulate():
    total = 0
    while True:
        x = (yield)
        if x is None:
            return total # StopItertaion
        total += x

def sum_coroutine():
    while True:
        total = yield from accumulate()
        print(total)

co = sum_coroutine()
next(co) # sum_coroutine -> accumulate

for i in range(1, 11):
    co.send(i) # accumulate
co.send(None) # 코루틴 accumulate에 None을 보내서 숫자 누적을 끝냄, accumulate -> sum_coroutine

for i in range(1, 101):
    co.send(i) # sum_coroutine -> accumulate
co.send(None) # accumulate -> sum_coroutine


# accumulate는 None을 받으면 코루틴이 완전히 끝나지만 
# sum_coroutine에서 무한 루프로 반복하고 있으므로 print로 total을 출력한 뒤 다시 yield from accumulate()로 accumulate를 실행