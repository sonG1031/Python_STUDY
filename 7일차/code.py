# kor, eng, math, sci = map(int, input().split())

# if 0 <= kor <= 100 and 0 <= eng <= 100 and 0 <= math <= 100 and 0 <= sci <= 100:
#     avg = (kor + eng + math + sci) / 4
#     if avg >= 80:
#         print('합격')
#     else:
#         print('불합격')
# else:
#     print('잘못된 점수')

age = int(input())
balance = 9000

if age >= 7 and age <= 12:
    balance -= 650
elif age >= 13 and age <= 18:
    balance -= 1050
else:
    balance -= 1250

print(balance)