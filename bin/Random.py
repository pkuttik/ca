def fib(n):
    curr = 1
    prev = 0
    counter = 0
    while counter < n:
        yield curr
        curr, prev = curr + prev, curr
        counter += 1
if __name__ == '__main__':
    # i,j = 0,1
    # for s in range(10):
    #     # print(s, end="")
    #     print(i, end=" ")
    #     i, j = i + j, i
    #
    # print(" Fib list")
    #
    fib_gen = fib(10)
    for _ in range(10):
        print(next(fib_gen), sep=",")
    print()