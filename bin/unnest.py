ip = (1,2,(1,2,(3,1)))
def unnest(p):
    ri = []
    for i in p:
        if isinstance(i,tuple):
            ri = ri + unnest(i)
            # ri.append(unnest(i))
        else:
            ri.append(i)
    return ri
print(unnest(ip))

