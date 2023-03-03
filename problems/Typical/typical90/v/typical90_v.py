A, B, C = map(int, input().split())

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

r = gcd(A, gcd(B, C))
print((A // r - 1) + (B // r - 1) + (C // r - 1))
