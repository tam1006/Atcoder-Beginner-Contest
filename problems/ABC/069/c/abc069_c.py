N = int(input())
a = list(map(int, input().split()))

odd = 0
two = 0
four = 0

for i in range(N):
    if a[i] % 2 != 0:
        odd += 1
    elif a[i] % 4 == 0:
        four += 1
    elif a[i] % 2 == 0:
        two += 1

if two == 0 and odd <= four + 1:
    print('Yes')
elif odd <= four:
    print('Yes')
else:
    print('No')