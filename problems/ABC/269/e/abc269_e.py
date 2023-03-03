#!/usr/bin/env python3
# from typing import *
import sys

sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().rstrip()
from functools import lru_cache

N = int(input())

A, B, C, D = 1, N, 1, N
U, D, L, R = 1, N, 1, N

for i in range(10):
    mid = (U+D)//2
    print(f"? {U} {mid} {L} {R}")
    T = int(input())

    if T == 0:


