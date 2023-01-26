class TimeIterator:
    def __init__(self, start, stop):
        self.current = start
        self.stop = stop

        self.hour = 0 if start // 3600 == 24 else start // 3600
        self.minute = (start % 3600) // 60
        self.sec = (start % 3600) % 60

        # 더 간단한 계산 방법
        # 하루는 24시간, 1시간은 60분, 1분은 60초인점을 이용
        # self.hour = start // 3600 % 24
        # self.minute = start // 60 % 60
        # self.sec = start % 60
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.stop:
            r = "{:02d}:{:02d}:{:02d}".format(self.hour, self.minute, self.sec)

            self.current += 1
            self.hour = 0 if self.current // 3600 == 24 else self.current // 3600
            self.minute = (self.current % 3600) // 60
            self.sec = (self.current % 3600) % 60
            
            return r
        else:
            raise StopIteration

    

    
    def __getitem__(self, index):
        self.current += index
        if self.current < self.stop:
            self.hour = 0 if self.current // 3600 == 24 else self.current // 3600
            self.minute = (self.current % 3600) // 60
            self.sec = (self.current % 3600) % 60

            return "{:02d}:{:02d}:{:02d}".format(self.hour, self.minute, self.sec)
        else:
            raise IndexError

start, stop, index = map(int, input().split())
 
for i in TimeIterator(start, stop):
    print(i)
 
print('\n', TimeIterator(start, stop)[index], sep='')
