from collections import Counter

def nC3(n):
    return n*(n-1)*(n-2)//6

def nC2(n):
    return n*(n-1)//2

N = int(input())
A = list(map(int, input().split()))

ans = nC3(N)
c = Counter(A)

for val in c.values():
    if val >= 2:
        ans -= nC2(val)*(N-val)
    if val >= 3:
        ans -= nC3(val)

print(ans)