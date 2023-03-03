# RMQ and RUQ

import sys
input = lambda: sys.stdin.readline().rstrip()
from typing import TypeVar, Callable, List
T = TypeVar('T')

# 0-indexed
class RangeMaximumUpdateQuery:
    def __init__(self, value: List[T], lazy: List[T],  identity: T, N: int, N0: int, LV: int):
        self.value = value
        self.lazy = lazy
        self.identity = identity
        self.N = N
        self.N0 = N0
        self.LV = LV

    # 初期値を配列Aで初期化, 全てidentityの値からの実行
    @classmethod
    def from_list(cls, A: List[T], identity: T):
        N = len(A)
        LV = (N-1).bit_length()
        N0 = 1 << LV

        value = [identity] * (N0 * 2)
        lazy = [0] * (N0 * 2)

        for i in range(N):
            value[i+N0] = A[i]

        for i in range(N0-1, 0, -1):
            value[i] = max(value[i*2], value[i*2+1])

        self = cls(value, lazy, identity, N, N0)
        return self


    # 大きさNで初期化
    @classmethod
    def new(cls, N: int, identity: T):
        LV = (N-1).bit_length()
        N0 = 1 << LV
        value = [identity] * (N0 * 2)
        lazy = [None] * (N0 * 2)
        return cls(value, lazy, identity, N, N0, LV)

    # 伝播対象の区間を求める
    def gindex(self, l, r):
        L = l + self.N0
        R = r + self.N0


        lm = (L // (L & -L)) >> 1
        rm = (R // (R & -R)) >> 1

        while L < R:
            if R <= rm:
                yield R
            if L <= lm:
                yield L
            L >>= 1
            R >>= 1

        while L:
            yield L
            L >>= 1

    # 伝播
    def propagates(self, *ids):
        for i in reversed(ids):
            v = self.lazy[i-1]
            if v is None:
                continue

            self.lazy[i*2-1] = v
            self.lazy[i*2] = v
            self.value[i*2-1] = v
            self.value[i*2] = v
            self.lazy[i-1] = None

    # 区間[l, r)をxで更新
    def update(self, l, r, x):
        assert 0 <= l <= r <= self.N

        *ids, = self.gindex(l, r)
        self.propagates(*ids)

        L = self.N0 + l
        R = self.N0 + r
        while L < R:
            if R & 1:
                R -= 1
                self.lazy[R-1] = x
                self.value[R-1] = x

            if L & 1:
                self.lazy[L-1] = x
                self.value[L-1] = x
                L += 1

            L >>= 1
            R >>= 1

        for i in ids:
            self.value[i-1] = max(self.value[i*2-1], self.value[i*2])

    # 区間[l, r)の最小値を取得
    def query(self, l, r):
        assert 0 <= l <= r <= self.N

        self.propagates(*self.gindex(l, r))

        L = self.N0 + l
        R = self.N0 + r

        s = self.identity
        while L < R:
            if R & 1:
                R -= 1
                s = max(s, self.value[R-1])

            if L & 1:
                s = max(s, self.value[L-1])
                L += 1

            L >>= 1
            R >>= 1

        return s


W, N = map(int, input().split())

RMUQ = RangeMaximumUpdateQuery.new(W, 0)

for _ in range(N):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    v = RMUQ.query(l, r+1)
    RMUQ.update(l, r+1, v+1)
    print(v+1)
