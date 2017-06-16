def reverse(s):
    if len(s) == 1:
        return s
    else:
        return reverse(s[1:]) + s[0]

def f(n):
    if n <= 1:
        return n
    else:
        return f(n-1) + f(n-2)

if __name__ == '__main__':
    print(f(6))
    # s=input('enter the palindrome string ')
    # if s == reverse(s):
    #     print("%s is a palindrome %s" % (s, reverse(s)))
    # else:
    #     print("%s is not a palindrome %s" % (s, reverse(s)))