
# s: set of integers
def mex(s):
    i = 0
    # "in" operation can be done in O(1) time, if s is set
    while i in s:
        i += 1
    return i

# a: list of integers
# x: max balue of grundy
def grundy(a, x):
    grundy = [0] * (x + 1)
    for i in range(1, x+1):
        s = set()
        for j in a:
            if i - j >= 0:
                s.add(grundy[i-j])

        grundy[i] = mex(s)

    return grundy

