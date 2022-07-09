N = int(input())

def divisor(n, N): 
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0 and n//i <= N:
            table.append(i)
            if i != n//i:
                table.append(n//i)
        i += 1
    return table

ans = 0
for i in range(1, N+1):
    div = divisor(i, N)
    ans += len(div)

print(ans)
