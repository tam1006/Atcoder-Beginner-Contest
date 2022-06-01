N = int(input())
S = input()

ans = 0

for i in range(10**3):
    pin = str(f'{i:03}')

    tmp = 0
    for s in S:
        if s == pin[tmp]:
            tmp += 1
            if tmp == 3:
                ans += 1
                break

print(ans)