def sum_coroutine():
    total = 0
    while True:
        x = (yield total) # 코루틴 바깥에서 값을 받아오면서 바깥으로 값을 전달
        total += x

co = sum_coroutine()
print(next(co))

print(co.send(1))
print(co.send(2))
print(co.send(3))

#이 코루틴의 동작 과정
# 1. 먼저 next(co)로 코루틴의 코드를 최초로 실행하면 x = (yield total)의 yield에서 total을 메인 루틴으로 전달하고 대기
# 2. co.send(1)로 1을 보내면 코루틴은 대기 상태에서 풀리고 x = (yield total)의 x = 부분이 실행된 뒤 total += x로 숫자를 누적
# 3. 이 코루틴은 while True:로 반복하는 구조이므로 다시 x = (yield total)의 yield에서 total을 메인 루틴으로 전달하고 대기
# 4. 그다음에 메인 루틴에서 print(co.send(1))과 같이 코루틴에서 나온 값을 출력