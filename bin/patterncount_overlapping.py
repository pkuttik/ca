#!/bin/python3

import sys
import re

def patternCount(s):
    print(re.findall(r'(?=(10+1))',s))
    return len(re.findall(r'(?=(10+1))',s))


# Complete this function

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = patternCount(s)
    print(result)