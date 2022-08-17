import turtle as t

n = 6
t.shape('turtle')
t.color('red') # 펜의 색을 빨간색으로 설정
t.begin_fill() # 색칠할 영역 시작
for i in range(n):
    t.forward(100)
    t.right(360/n) # 다각형에서 외각의 합은 항상 360도
t.end_fill() # 색칠할 영역 끝
t.mainloop()