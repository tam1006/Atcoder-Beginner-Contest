N, Y = map(int, input().split())

for i in range(N+1):
    for j in range(N+1):
        if i+j > N:
            break

        if i*10 + j*5 + (N-i-j)*1 == Y//1000:
            print(i, j, N-i-j)
            exit()

print(-1, -1, -1)