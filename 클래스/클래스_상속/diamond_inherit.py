class A:
    def greeting(self):
        print("Hi, I'm A.")

class B(A):
    def greeting(self):
        print("Hi, I'm B.")

class C(A):
    def greeting(self):
        print("Hi, I'm C.")

class D(B, C):
    pass

x = D()
x.greeting() # Hi, I'm B.
# 이렇게 명확하지 않고 애매한 상태이기 때문에 다이아몬드 상속은 문제가 많다고 해서 죽음의 다이아몬드라고도 부릅니다.
print(D.mro()) # 메서드 탐색 순서