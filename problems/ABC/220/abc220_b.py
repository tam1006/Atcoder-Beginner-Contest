K = int(input())
A, B = map(int, input().split())

# def KtoTen(K, X):
#     ans = 0
#     for i, x in enumerate(str(X)[::-1]):
#         ans += int(x)*K**i
#     return ans

# A = KtoTen(K, A)
# B = KtoTen(K, B)

A = int(str(A), K)
B = int(str(B), K)

print(A*B)