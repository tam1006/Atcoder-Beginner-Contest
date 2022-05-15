N, W = map(int, input().split())
A = list(map(int, input().split()))
A.append(0)

weight = []
for i in range(N+1):
    weight.append(A[i])
    for j in range(i, N+1):
        if j == i:
            continue
        weight.append(A[i]+A[j])
        for k in range(j, N+1):
            if k == j or k == i:
                continue
            weight.append(A[i] + A[j] + A[k])

weight = list(set(weight))
weight.sort()

ans = 0
for w in weight:
    if w <= W:
        ans += 1
    else:
        break

print(ans-1)