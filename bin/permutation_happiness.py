#!/bin/python3

import sys
from itertools import permutations

def query(n, k):
    # Complete this function
    total = 0
    cntDict = {}
    cnt2 = 0
    s =sorted(list(permutations(range(1, n + 1))))
    # mods = s + []
    # for i in range(int(len(s)/2)):
    #     mods.remove(reversed(s[i]))
    # print(s[::2])
    # print(list(reversed(s[1::2])))
    # print(s[int(len(s) / 2) :])
    # print(s[:int(len(s) / 2) ])
    completedList = {}
    for p in s:
        happyPersons = 0
        if tuple(reversed(p)) not in completedList:
            happyPersons = sum(list(map (lambda x,y,z: 1 if x<y or x<z else 0, list(p), [0] + list(p)[:len(p)-1:], list(p)[1::] + [0])))
            # for i in range(n):
            #     if ((i != n-1 and p[i] < p[i+1]) or (i !=0 and p[i] < p[i-1])):
            #     # if ((i != n-1 and p[i] < p[i+1]) or (i !=0 and p[i] < p[i-1])):
            #         happy += 1
            #         if k == happy:
            #              # break
            #             pass
            #         hp[p[i]] = 1
            #     else:
            #         unhappy += 1
            #         hp[p[i]] = 0
            #         if maxout == unhappy:
            #             # break
            #             pass

                # if i != n-1  and i != 0 and p[i] == 3 and p[i+1] == 2 and p[i-1] == 1:
                #     print(p, happy)
                #     cnt2 += 1
            completedList[p] = 1 if k <= happyPersons else 0
            total += 1 if k <= happyPersons else 0

            print(p, happyPersons)
        else:
            completedList[tuple(reversed(p))] = completedList.get(tuple(reversed(p))) + completedList.get(tuple(reversed(p)))
        # if happy > 1:
        # cntDict [happy] = cntDict.get(happy, 0) + 1


    # print(cntDict)
    # print('Completed list {}'.format(completedList))
    # print(cnt2)
    return (total*2)%(10**9 + 7)

# q = int(input().strip())
for a0 in range(1):
    # n, k = input().strip().split(' ')
    # n, k = [int(n), int(k)]
    # Find the number of ways to arrange 'n' people such that at least 'k' of them will be happy
    # The return value must be modulo 10^9 + 7
    n= 6
    k =1
    result = query(n, k)
    print(result)

#5,3 {2: 16, 3: 104}
#4,3 {2: 16, 3: 8}
#6,5 {3: 272, 4: 416, 5: 32}