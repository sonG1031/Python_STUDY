def fib(n):
    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a+b
    return b

def recurisve_fib(n):
    if n == 1 or n == 0:
        return n
    return recurisve_fib(n-1) + recurisve_fib(n-2)

n = int(input())
print('for', fib(n))
print('recursive', recurisve_fib(n))