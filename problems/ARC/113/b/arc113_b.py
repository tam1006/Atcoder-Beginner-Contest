A, B, C = map(int, input().split())

C = C % 4
if C == 0:
    C = 4

B = B % 4

if B == 0:
    B = 4

ans = (int(str(A)[-1]) ** B ** C) % 10
print(ans)