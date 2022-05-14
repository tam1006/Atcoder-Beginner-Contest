N = int(input())
a = [int(input()) for _ in range(N)]

light = 1
for i in range(N):
    if a[light-1] == 2:
        print(i+1)
        exit()
    
    light = a[light-1]

print(-1)