N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

def check(x):
    count = 0
    left = 0
    for right in A:
        if right - left < x or L - right < x:
            continue
        count += 1
        left = right
    return count >= K

l = 0
r = 10**9 + 1

while r - l > 1:
    mid = (l + r) // 2
    if check(mid):
        l = mid
    else:
        r = mid

print(l)
