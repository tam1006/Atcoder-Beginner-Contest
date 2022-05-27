A, B, C, X, Y = map(int, input().split())


if X >= Y:
    ans = min(A, 2*C)*(X-Y) + min(A+B, 2*C)*Y
else:
    ans = min(B, 2*C)*(Y-X) + min(A+B, 2*C)*X

print(ans)