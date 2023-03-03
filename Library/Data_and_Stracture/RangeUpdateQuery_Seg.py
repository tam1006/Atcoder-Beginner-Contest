# Range Update Query Segment Tree

from typing import TypeVar, Callable, List
T = TypeVar('T')

# l, r, xが与えられた時、[l, r)の値をxに更新 O(logN)
# xが与えられた時、xの値を返す O(logN)
# 更新は、その時刻tを含む(t, x)のtupleで更新し、値を取得するときはtの最大値のxを取ってくる
# 1-indexed
class RangeUpdateQuery:
    def __init__(self, data: List[T], N: int, N0: int):
        self.data = data
        self.N = N
        self.N0 = N0

    # 初期値を配列Aで初期化, 全てidentityの値からの実行
    @classmethod
    def from_list(cls, A: List[T]):
        N = len(A)
        N0 = 1 << (N - 1).bit_length()

        data = [(-1, 0)] * (2 * N0)

        for i in range(N):
            data[N0 + i] = (0, A[i])

        return cls(data, N, N0)

    # 長さNの配列を作成, 全てidentityの値で初期化
    @classmethod
    def new(cls, N: int, identity: T):
        N0 = 1 << (N - 1).bit_length()
        data = [(0, identity)] * (2 * N0)

        return cls(data, N, N0)

    # i番目の値を返す O(logN)
    def get(self, i: int) -> int:
        assert 1 <= i <= self.N

        i += self.N0 - 1
        x = (-1, -1)
        while i > 0:
            x = max(x, self.data[i])
            i = i >> 1

        return x[1]

    # [l, r)を時刻tにxで更新する O(logN)
    def range_update(self, l: int, r: int, t: int, x: T):
        assert 1 <= l < r <= self.N + 1

        l += self.N0 - 1
        r += self.N0 - 1

        while l < r:
            if l & 1:
                self.data[l] = (t, x)
                l += 1
            if r & 1:
                r -= 1
                self.data[r] = (t, x)
            l = l >> 1
            r = r >> 1

# https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_D

N, Q = map(int, input().split())
RUQ = RangeUpdateQuery.new(N, (1 << 31) - 1)

for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 0:
        s, t, x = q[1:]
        s += 1
        t += 1
        RUQ.range_update(s, t + 1, i+1, x)
    else:
        i = q[1]
        i += 1
        print(RUQ.get(i))
