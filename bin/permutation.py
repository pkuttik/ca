from itertools import permutations
from itertools import combinations

# for i in set(permutations('00011',5)):
#     print(5)
#     print(''.join(i))
for i in permutations(range(1,5+1)):
    print(i)
print(list(combinations(['a','b','c'], 2)))

