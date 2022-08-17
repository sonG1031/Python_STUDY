import turtle as t

n = int(input())
t.shape('turtle')
for i in range(n):
    t.forward(100)
    t.right(360/n) # 다각형에서 외각의 합은 항상 360도

t.mainloop()

# 프로그래밍은 이런 방식으로 소스 코드를 일반화해 나가는 과정
# 즉, 공통된 부분을 일반화해서 원하는 결과를 얻어내는 과정이 프로그래밍이며 컴퓨테이셔널 씽킹.