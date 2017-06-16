import timeit
from timeit import Timer

def csort(cinput):
    clen = len(cinput)
    swap = False
    try:
        for i in range(clen):
            for j in range(i,clen):
                if cinput[i] > cinput[j]:
                    cinput[i], cinput[j] = cinput[j], cinput[i]
                    print("at %s input is %s " %(i ,cinput))
        return cinput
    except TypeError as ve:
        print('csort says give me only integer')

def bsort(cinput):
    clen = len(cinput)
    swap = False
    try:
        for i in range(clen-1, 0, -1):
            swap=False
            for j in range(i):
                if cinput[j] > cinput[j+1]:
                    cinput[j], cinput[j+1] = cinput[j+1], cinput[j]
                    # print("at %s input is %s " %(i ,cinput))
                    swap = True
            # print ("pass {}".format(i))
            if swap == False:
                break
                # pass
        print(cinput)
        return cinput
    except TypeError as ve:
        print('csort says give me only integer')

def isort(cinput):
    clen = len(cinput)
    for i in range(1, clen):
        currvalue = cinput[i]
        pointer = i
        while pointer > 0 and currvalue < cinput[pointer - 1]:
            cinput[pointer] = cinput[pointer - 1]
            pointer -= 1
        cinput[pointer] = currvalue
    print(cinput)

if __name__ == '__main__':
    # inp = [56,90,45,2,25,78,100.0,6,45,67]
    inp = [56,90,45,2,25,78,100.0,6,45,67, 113, 112]
    isort(inp)
    # inp = [1,2,3,4,5]
    # t = Timer("csort(inp)","from __main__ import csort, inp")
    # t = Timer("bsort(inp)","from __main__ import bsort, inp")
    # print(bsort(inp))
    # print(t.timeit(10000))
