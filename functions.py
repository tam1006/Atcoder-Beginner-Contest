#a,bの最大公約数
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

#a,bの最小公倍数
def lcm(a, b):
    return a * b // gcd (a, b)

#nの約数を全て求める
def divisor(n): 
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table

#nを素因数分解したリストを返す
def prime_decomposition(n):
  i = 2
  table = []
  while i * i <= n:
    while n % i == 0:
      n /= i
      table.append(int(i))
    i += 1
  if n > 1:
    table.append(int(n))
  table.sort()
  return table

# 素因数分解
# 460 = 2^2 x 5 x 23 の場合
# 返り値は [(2, 2), (5, 1), (23, 1)]
def prime_factorize(N):
    res = []
    for p in range(2, N):
        if p * p > N:
            break
        if N % p != 0:
            continue
        e = 0
        while N % p == 0:
            e += 1
            N //= p
        res.append((p, e))
    if N != 1:
        res.append((N, 1))
    return res

#引数nが素数かどうかを判定
def is_prime(n):
    for i in range(2, n + 1):
        if i * i > n:
            break
        if n % i == 0:
            return False
    return n != 1

# 引数以下の全ての素数を返す
# エラトステネスの篩
def sieve(n):
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = False

    for i in range(2, n+1):
        if is_prime[i-1]:
            j = 2 * i
            while j <= n:
                is_prime[j-1] = False
                j += i
    table = [ i for i in range(1, n+1) if is_prime[i-1]]
    return is_prime, table

#xのn乗をmで割った余り
def pos(x, n, m):
    if n == 0:
        return 1
    res = pos(x*x%m, n//2, m)
    if n%2 == 1:
        res = res*x%m
    return res

# nビット生成
def bit(n):
    import itertools
    L = [0, 1] #生成する数字
    bit_list = list(itertools.product([0, 1], repeat=n))
    return bit_list

# 階乗
def factorial(n):
    import math
    return math.factorial(n)

# nPr(順列)
def nPr(n, r):
    import math
    return math.factorial(n) // math.factorial(n-r)

# nCr(組み合わせ)
def nCr(n, r):
    import math
    return math.factorial(n) // (math.factorial(n-r) * math.factorial(r))




if __name__ == '__main__':
    print(nCr(60, 30))