# start, stop = map(int, input().split())

# i = start

# while True:
#     if i % 10 == 3:
#         i += 1
#         continue
#     if i > stop:
#         break
#     print(i, end=' ')
#     i += 1

# from turtle import width


# for i in range(5):
#     for j in range(5):
#         print('j:', j, sep='', end=' ')
#     print('i:', i, '\\n', sep='')
# # result:
# # j:0 j:1 j:2 j:3 j:4 i:0\n
# # j:0 j:1 j:2 j:3 j:4 i:1\n
# # j:0 j:1 j:2 j:3 j:4 i:2\n
# # j:0 j:1 j:2 j:3 j:4 i:3\n
# # j:0 j:1 j:2 j:3 j:4 i:4\n

# for i in range(5):
#     for j in range(5):
#         if i == j: 
#             print('*', end='')
#         else:
#             print(end=' ')
#     print()

# for i in range(5):
#     for j in range(5):
#         if j <= i: 
#             print('*', end='')
#     print()

# for i in range(5):
#     for j in range(5):
#         if j < i: 
#             print(end=' ')
#         else:
#             print('*', end='')
#     print()




# a = 3
# for i in range(2, -1, -1):
#     for j in range(a):
#         if j < i: 
#             print(end=' ')
#         else:
#             print('*', end='')
#     print()
#     a += 1

# height = int(input())
# width = height

# for i in range(height-1, -1, -1):
#     for j in range(width):
#         if j < i: 
#             print(end=' ')
#         else:
#             print('*', end='')
#     print()
#     width +=1

height = int(input()) # 3

for i in range(height): # i: 0 1 2
    for j in reversed(range(height)): # j: 2 1 0
        if i < j:
            print(' ', end='')
        else:
            print('*', end='')
    for j in range(height): # j: 0 1 2
        if i > j:
            print('*', end='')
    print()