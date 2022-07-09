N, x = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
i = 0

while x > 0:
    if i == N:
        break
    x -= a[i]
    i += 1

if x != 0:
    i -= 1
print(i)