import sys

# 현재 객체가 몇 번 사용되었는지 확인
print(sys.getrefcount(1000)) # 2: Windows에서 처음 레퍼런스 카운트는 2
                             # 3: 리눅스에서 처음 레퍼런스 카운트는 3, sys.getrefcount를 호출하면서 내부적으로 1000을 두 번 사용했기 때문.

x = 1000
print(sys.getrefcount(1000))

y = 1000
print(sys.getrefcount(1000))

print(x is y) # True

# 첫 번째 값이 거짓이므로 두 번째 값은 확인하지 않고 거짓으로 결정
print(False and True)     # False