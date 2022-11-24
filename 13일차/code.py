# [[[0] * 3 for i in range(4)] for i in range(2)]
# [[[0 for col in range(3)] for row in range(4)] for depth in range(2)]

col, row = map(int, input().split())
a = []

for i in range(row):
    # b = []
    # # string = input()
    # # for j in string:
    # #     b.append(j)
    # a.append(b)
    a.append(list(input()))

result = []
# for i in range(len(a)): # 무식한 방법ㅎ
    # cnt = 0
    # tmp = []
    # for j in range(len(a[i])):
    #     if a[i][j] == '.':
    #         if i >= 1 and a[i-1][j] == '*': # 위
    #             cnt += 1
    #         if i < len(a)-1 and a[i+1][j] == '*': # 아래
    #             cnt += 1
    #         if j >= 1 and a[i][j-1] == '*': # 왼쪽
    #             cnt += 1
    #         if j < len(a[i])-1 and a[i][j+1] == '*': # 오른쪽
    #             cnt += 1
    #         if j >= 1 and i >= 1 and a[i-1][j-1] == '*': # 왼쪽 위 대각선
    #             cnt += 1
    #         if j < len(a[i])-1 and i >= 1 and a[i-1][j+1] == '*': # 오른쪽 위 대각선
    #             cnt += 1
    #         if j < len(a[i])-1 and i < len(a)-1 and a[i+1][j+1] == '*': # 오른쪽 아래 대각선
    #             cnt += 1
    #         if j >= 1 and i < len(a)-1 and a[i+1][j-1] == '*':
    #             cnt += 1
    #         tmp.append(cnt)
    #     else:
    #         tmp.append(a[i][j])
    #     cnt = 0
    # result.append(tmp)
for i in range(row):
    tmp = []
    for j in range(col):

        if a[i][j] == '.':
            cnt = 0
            for y in range(i-1, i+2): # 한 칸 위부터 한 칸 아래까지 반복
                for x in range(j-1, j+2): # 한 칸 앞(왼쪽)부터 한 칸 뒤(오른쪽)까지 반복
                    if y >= 0 and x >= 0 and y < row and x < col: # 적절한 인덱스인지 확인
                        if a[y][x] == '*':
                            cnt += 1
            tmp.append(cnt)
        else:
            tmp.append('*')
    result.append(tmp)
                        


for i in result:
    for j in i:
        print(j, end='')
    print()