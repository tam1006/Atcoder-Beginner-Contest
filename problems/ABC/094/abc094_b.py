N, M, X = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

maze = [0] * (N + 1)
for a in A:
    maze[a] = 1

ans = min(sum(maze[0:X+1]), sum(maze[X:]))
print(ans)