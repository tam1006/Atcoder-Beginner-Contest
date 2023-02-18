N = int(input())

# https://zenn.dev/erbowl/articles/22d6b56177a81f

def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

p = pow(10, 9) + 7
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]
 
for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

for k in range(1, N+1):
    ans = 0
    for a in range(1, N+1):
        if N - (k-1)*(a-1) < a:
            break
        ans += cmb(N-(k-1)*(a-1), a, p) % p
        ans %= p
    print(ans)

