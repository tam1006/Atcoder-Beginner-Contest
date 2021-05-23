n = int(input())
a = input().split()
b = input().split()
c = input().split()

g = [int(0)]*(n+1)
for i in range(n):
    g[int(b[int(c[i])-1])] += 1

ans = 0
for i in range(n):
    ans += int(g[int(a[i])])

print(ans)