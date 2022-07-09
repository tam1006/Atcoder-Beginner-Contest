N = int(input())
p = list(int(input()) for _ in range(N))

p.sort()

print(sum(p) - p[-1]//2)