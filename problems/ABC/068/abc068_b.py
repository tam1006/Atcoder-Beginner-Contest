N = int(input())

ans = 1

while ans < N:
    if ans*2 <= N:
        ans *= 2
    else:
        break

print(ans)