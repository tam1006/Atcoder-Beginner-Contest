MOD = pow(10, 9) + 7

def dot(A, B):
    Ah, Bh, Bw = len(A), len(B), len(B[0])
    C = [[0 for _ in range(Bw)] for _ in range(Ah)]
    for i in range(Ah):
        for j in range(Bw):
            for k in range(Bh):
                C[i][j] += A[i][k] * B[k][j] % MOD
                C[i][j] %= MOD
    return C

# Mのk乗を効率的に計算する
def powmat(M, k):
    k -= 1
    Mc = M.copy()
    while k > 0:
        if k & 1 == 1:
            Mc = dot(Mc, M)
        M = dot(M, M) # Mの(2のi乗)の乗 を計算する
        k >>= 1
    return Mc

# limit 以下の全ての素数を返す: エラトステネスの篩
def list_primes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False

    for p in range (0, limit + 1):
        if not is_prime[p]:
            continue
        primes.append(p)
        for i in range(p*p, limit + 1, p):
            is_prime[i] = False

    return primes



# cmb mod M の、逆元を用いた高速化
# https://blog.satoooh.com/entry/5195/
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

N = pow(10, 6)

for i in range(2, N+1):
    fact.append((fact[-1] * i) % MOD)
    inv.append((-inv[MOD%i] * (MOD // i) % MOD))
    factinv.append(((factinv[-1] * inv[-1]) % MOD))

def cmb(n, r, p):
    if (r < 0) or n < r:
        return 0

    r = min(r, n-r)
    return fact[n] * factinv[r] * factinv[n-r] % p

print(cmb(6000, 4343, MOD))
