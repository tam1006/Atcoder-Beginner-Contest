N, X = map(int, input().split())

S = ''
for i in range(26):
    S += chr(ord('A')+i)*N 

print(S[X-1])