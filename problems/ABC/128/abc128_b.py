N = int(input())
SP = []
for i in range(N):
    s, p = input().split()
    SP.append((s, -int(p), i+1))

SP.sort(key=lambda x: (x[0], x[1]))
for _, _, i in SP:
    print(i)