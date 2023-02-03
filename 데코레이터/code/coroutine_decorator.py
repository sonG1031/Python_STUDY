def coroutine(func):
    def init(*args, **kwargs):
        co = func(*args, **kwargs)
        next(co)
        return co
    return init

@coroutine
def sum_coroutine():
    total = 0
    while True:
        x = (yield total)
        total += x

co = sum_coroutine()

print(co.send(1))
print(co.send(2))
print(co.send(3))
