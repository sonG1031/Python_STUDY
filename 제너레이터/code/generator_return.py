def generator():
    yield 1
    return "return value"

try:
    g = generator()
    print(next(g))
    print(next(g))
except StopIteration as e:
    print(e)