N = int(input())
A = list(map(int, input().split()))

args = [0 for _ in range(N+2)]
args[-1] = 360

for i in range(N):
    args[i+1] = (A[i] + args[i]) % 360

args.sort()
ans = 0
for i in range(N+1):
    if args[i+1] - args[i] > ans:
        ans = args[i+1] - args[i]

print(ans)