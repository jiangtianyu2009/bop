def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


if __name__ == "__main__":
    g = (x * x for x in range(10))
    for n in g:
        print(n)
    for x in fib(8):
        print(x)
