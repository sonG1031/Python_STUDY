# string = input()
# ngram = int(input()) # 몇 n으로 할지 선택
# for i in range(len(string)-ngram+1):
#     print(string[i:i+ngram])

text = 'hello'
three_gram = list(zip(*[text[i:] for i in range(3)]))
print(three_gram)
# 리스트에 *를 붙이는 방법은 리스트 언패킹(list unpacking)
for i in three_gram:
    print(i[0], i[1], i[2], sep='')