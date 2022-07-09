N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

from itertools import permutations

num_list = list(permutations(range(1, N+1)))

print(abs(num_list.index(P) - num_list.index(Q)))