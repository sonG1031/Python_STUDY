def iterable_generator():
    x = [1, 2, 3]
    yield from x

def number_generator(stop):
    n = 0
    while n < stop:
        yield n
        n += 1

def generator_generator():
    yield from number_generator(3)

for i in iterable_generator():
    print(i)

for i in generator_generator():
    print(i)