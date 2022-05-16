N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

ans = [float('inf'), -1]

for i in range(N):
    diff = abs(T - H[i]*0.006 - A)
    if diff < ans[0]:
        ans[0] = diff
        ans[1] = i+1

print(ans[1])