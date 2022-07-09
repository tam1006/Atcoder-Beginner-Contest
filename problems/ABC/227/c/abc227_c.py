N = int(input())

ans = 0

for a in range(1, int((N+1)**(1/3))+1):
    for b in range(a, int(((N+1)/a)**(1/2))+1):
        if  N // (a*b) - b < 0:
            continue
        ans +=  N // (a*b) - b + 1

print(ans)
