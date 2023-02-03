class Trace:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        r = self.func(*args, **kwargs)
        print(f"{self.func.__name__}(args={args}, kwargs={kwargs}) -> {r}")

        return r

@Trace
def add(a,b):
    return a + b

print(add(10,20))
print(add(a=10,b=20))