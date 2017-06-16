hexdigit='0123456789ABCDEFGH'
def bc(n, base):
    if (n<base):
        return n
    return str(bc(n//base,base)) + str(hexdigit[n%base])
print (bc(26,16))