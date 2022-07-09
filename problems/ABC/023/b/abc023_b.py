N = int(input())
S = input()

name = 'b'

if N % 2 == 0:
    print(-1)
    exit()

for i in range(1, N//2+1):
    if i % 3 == 0:
        name = 'b' + name + 'b'
    elif i % 3 == 1:
        name = 'a' + name + 'c'
    else:
        name = 'c' + name + 'a'

if name == S:
    print(N//2)
else:
    print(-1)