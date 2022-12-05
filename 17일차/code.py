import pickle

# string = '갱갱갱'
# integer = 18
# dictionary = {'key' : 'value'}

# with open('test.p', 'wb') as file: #b는 바이너리(binary)를 뜻함. 바이너리 파일은 컴퓨터가 처리하는 파일 형식
#     pickle.dump(string, file)
#     pickle.dump(integer, file)
#     pickle.dump(dictionary, file)

# with open('test.p', 'rb') as file: # 파일을 바이너리 읽기 모드(rb)로 열기
#     for i in range(3):
#         print(pickle.load(file))

with open('words.txt', 'r') as file:
    s = file.read().split()
    for i in s:
        if 'c' in i:
            print(i.strip(',.'))