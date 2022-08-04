keys = input().split()
vals = map(float, input().split())

result = dict(zip(keys, vals))
print(result)