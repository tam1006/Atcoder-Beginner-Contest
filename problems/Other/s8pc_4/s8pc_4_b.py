N, K = map(int, input().split())
a = list(map(int, input().split()))

ans = float('inf')
for i in range(2**N):
    money = 0
    building = [0]*N
    for j in range(N):
        if ((i >> j) & 1):
            building[j] = 1
    
    if sum(building) < K:
        continue
    
    highest = 0
    for j in range(N):
        if j == 0:
            continue

        highest = max(highest, a[j-1])
        if building[j] == 1:
            if a[j] <= highest:
                money += (highest - a[j] + 1)
                highest += 1
        
    ans = min(ans, money)


print(ans)