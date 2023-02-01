def number_coroutine():
    while True: # 코루틴을 유지하기 위해 무한 루프
        x = (yield) # 메인 루틴에서 받아온 값
        print(x)

co = number_coroutine()
print(type(co))
print(dir(co))
next(co) # 최초 실행하여 yield까지 코드를 실행

co.send(1)
co.send(2)
co.send(3)

# 이 코루틴의 동작 과정
# 1. 먼저 next(co)로 코루틴의 코드를 최초로 실행하면 x = (yield)의 yield에서 대기하고 다시 메인 루틴으로 돌아옵니다.
# 2. 그다음에 메인 루틴에서 co.send(1)로 1을 보내면 코루틴은 대기 상태에서 풀리고 x = (yield)의 x = 부분이 실행된 뒤 print(x)로 숫자를 출력
# 3. 이 코루틴은 while True:로 반복하는 구조이므로 다시 x = (yield)의 yield에서 대기, 그러고 나서 메인 루틴으로 돌아옵니다.