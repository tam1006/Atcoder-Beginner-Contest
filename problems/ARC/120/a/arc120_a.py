n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    a[i] += a_max
    a_max = max(a_max, a[i])
