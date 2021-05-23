from collections import deque

a,b,k = map(int, input().split())
# k -= 1
# nCr(組み合わせ)
def nCr(n, r):
    import math
    return math.factorial(n) // (math.factorial(n-r) * math.factorial(r))

n = nCr(a+b, a)

ans = deque([])

def binary(i, low, an, bn):
    print(nCr(a+b-i, a-i))
    if k <= nCr(a+b-i, a-an)+low:
        ans.append("a")
        if nCr(a+b-i, a-an) == 1:
            return
        binary(i+1, low)
    else:
        ans.append("b")
        if nCr(a+b-i, b-bn) == 1:
            return
        binary(i+1, nCr(a+b-i, a-an)+low)

binary(1, 0, a, b)
print(ans)