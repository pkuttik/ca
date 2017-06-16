def g(*l):
    total = 0
    for i in l:
        total += i
        yield  total

if __name__ == '__main__':
    csum = g(1,2,3,2)
    print(*list(csum), type(csum), sep = '\n'+'-->'*2)