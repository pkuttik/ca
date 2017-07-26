#!/bin/python3

import sys, math, itertools, operator

def maximumGcdAndSum(A, B):
    # Complete this function
    A.sort(reverse=True)
    B.sort(reverse =True)
    A = sorted(set(A), reverse=True)
    B = sorted(set(B), reverse=True)

    pgcd = 0
    gcdl = {}
    gcdl[0] = [1]
    tsum = 0
    for i in itertools.product(A, B):
        print ([i, pgcd], end= ' ')
        if pgcd > i[0] // 2 and pgcd > i[1] // 2:
            break
        cgcd = math.gcd(i[0], i[1])

        if cgcd == pgcd:
            if tsum < i[0] + i[1]:
                tsum = i[0] + i[1]
                pgcd = cgcd
        elif cgcd > pgcd:
            # gcdl[cgcd] = [i] if cgcd not in gcdl else gcdl[cgcd] + [i]
            tsum = i[0] + i[1]
            pgcd = cgcd
            # fgcd = max(gcdl.items(), key=operator.itemgetter(0))[0]

    print(pgcd , gcdl)
    print(sorted(list(itertools.product(A, B)),key = lambda x:x[0] + x[1], reverse=True))
    return tsum
    fgcd = max(gcdl.items(), key=operator.itemgetter(0))[0]
    # return max(sum(i) for i in gcdl[pgcd])


    # l = sorted([(math.gcd(i[0],i[1]), i) for i in list(itertools.product(A,B))], key = lambda x: (x[0],sum(x[1])), reverse = True)
    # maxGcd = l[0][0]

    # m=[]
    # for i in l:
    #     if i[0] != maxGcd:
    #         break
    #     else:
    #         m.append(i[1])
    # return max([sum(i) for i in m])
    # return sum(l[0][1])

if __name__ == "__main__":
    n = int(input().strip())
    A = list(map(int, input().strip().split(' ')))
    B = list(map(int, input().strip().split(' ')))
    res = maximumGcdAndSum(A, B)
    print(res)
