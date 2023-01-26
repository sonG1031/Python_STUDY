class Counter:
    def __init__(self, stop):
        self.current = 0
        self.stop = stop

    def __iter__(self):
        # 이 객체는 리스트, 문자열, 딕셔너리, 세트, range처럼 __iter__를 호출해줄 반복 가능한 객체(iterable)가 없으므로 현재 인스턴스를 반환
        # 즉, 이 객체는 반복 가능한 객체이면서 이터레이터입니다.
        return self
    
    def __next__(self):
        if self.current < self.stop:
            r = self.current
            self.current += 1
            return r
        else:
            raise StopIteration
        

for i in Counter(3):
    print(i, end=' ')