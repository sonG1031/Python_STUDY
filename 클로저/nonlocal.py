def A():
    x = 10
    y = 100
    def B():
        x = 20
        def C():
            nonlocal x # 20, 가장 가까운 x는 B함수의 지역 범위에 있음.
            nonlocal y # 100

            x = x + 30
            y = y + 300
            print(x)
            print(y)
        C()
    B()

A()