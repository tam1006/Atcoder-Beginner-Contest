N = int(input())
A, B, C = map(int, input().split())

MAX = 9999

ans = MAX
for a in range(MAX):
    for b in range(MAX):
        if a*A + b*B > N:
            break

        if (N - a*A - b*B) % C == 0:
            c = (N - a*A - b*B) // C
            ans = min(ans, a+b+c)


print(ans)
