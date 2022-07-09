N, M, X, T, D = map(int, input().split())


a = T - min(N, X)*D
print(a + min(X, M)*D)