A, B, K, L = map(int, input().split())

import math

ans = min(B*math.ceil(K/L), B*(K//L) + A*(K%L))

print(ans)