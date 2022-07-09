N, A, B = map(int, input().split())

print((N//(A+B))*A + max(0, min(N%(A+B), A)))