import sys

n = int(sys.stdin.readline())

count_fib = 0


def fib(a):
    global count_fib
    if a == 1 or a == 2:
        count_fib += 1
        return 1
    else:
        return fib(a - 1) + fib(a - 2)


f = [0] * (n)
count_fibon = 0


def fibonacci(a):
    global count_fibon
    f[0] = 1
    f[1] = 1
    for i in range(2, a):
        f[i] = f[i-1] + f[i-2]
        count_fibon += 1
    return f[a-1]




fib(n)
fibonacci(n)

print(count_fib, count_fibon)
