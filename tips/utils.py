MOD = 998244353

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
