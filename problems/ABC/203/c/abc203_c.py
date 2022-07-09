import numpy as np

n, k = map(int, input().split())
ab = []
for i in range(n):
    ab.append(list(map(int, input().split())))

ab = sorted(ab)
# print(ab)
for distance, money in ab:
    # print(distance, money)
    if distance <= k:
        k += money
print(k)