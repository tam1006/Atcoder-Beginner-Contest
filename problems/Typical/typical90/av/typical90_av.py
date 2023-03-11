N, K = map(int, input().split())
points = []
for _ in range(N):
    A, B = map(int, input().split())
    points.append(B)
    points.append(A-B)

points.sort(reverse=True)
print(sum(points[:K]))
