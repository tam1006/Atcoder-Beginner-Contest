# RSQ and RAQ

# 二つのBITを用いることで表現できる。
# 範囲加算と範囲和のクエリをそれぞれO(logN)で処理できる。

from typing import TypeVar, Callable, List
T = TypeVar('T')

class RangeSumQuery:
    def __init__(self, data: List[T], identity: T, N: int):
        self.data = data
        self.identity = identity
        self.N = N

    # 初期値を配列Aで初期化, 全てidentityの値からの実行
    @classmethod
    def from_list(cls, A: List[T], identity: T):
        N = len(A)
        data = [identity] * (N + 1)
        self = cls(data, identity, N)
        for i in range(N):
            self.add(i+1, A[i])
        return self

    @classmethod
    def new(cls, size: int, identity: T):
        data = [identity] * (size + 1)
        return cls(data, identity, size)

    # i番目の値にxを加算する
    def add(self, i: int, x: T):
        assert 1 <= i <= self.N+1

        while i <= self.N:
            self.data[i] += x
            i += i & -i

    # [0, i]の和, 1-indexed, i=0なら0を返す
    def sum(self, i) -> T:
        assert 0 <= i <= self.N

        s = self.identity
        while i > 0:
            s += self.data[i]
            i -= i & -i

        return s

    # [l, r)の和, 1-indexed, l=rなら0を返す
    def range_sum(self, l: int, r: int) -> T:
        assert 0 <= l <= r <= self.N+1

        return self.sum(r-1) - self.sum(l-1)

    # i番目の値を取得する
    def get(self, i: int) -> T:
        assert 1 <= i <= self.N

        return self.range_sum(i, i+1)

    # i番目の値をxに更新する
    def update(self, i: int, x: T):
        assert 1 <= i <= self.N

        self.add(i, x - self.get(i))

# 1-indexed
class RangeAddSumQuery:
    def __init__(self, bit1: RangeSumQuery, bit2: RangeSumQuery, identity: T, N:int):
        self.bit1 = bit1
        self.bit2 = bit2
        self.identity = identity
        self.N = N

    # 初期値を配列Aで初期化, 全てidentityの値からの実行
    @classmethod
    def from_list(cls, A: List[T], identity: T):
        N = len(A)
        bit1 = RangeSumQuery.new(N, identity)
        bit2 = RangeSumQuery.new(N, identity)
        self = cls(bit1, bit2, identity, N)
        for i in range(len(A)):
            self.add(i+1, A[i])
        return self

    # 初期値を全てidentityの値からの実行
    @classmethod
    def new(cls, size: int, identity: T):
        N = size
        bit1 = RangeSumQuery.new(N, identity)
        bit2 = RangeSumQuery.new(N, identity)
        return cls(bit1, bit2, identity, N)

    # [l, r)にxを加算する
    def add(self, l: int, r: int, x: T):
        assert 1 <= l <= r <= self.N+1

        self.bit1.add(l, -x * (l-1))
        self.bit1.add(r, x * (r-1))
        self.bit2.add(l, x)
        self.bit2.add(r, -x)

    # [0, i]の和, 1-indexed, i=0なら0を返す
    def sum(self, i: int) -> T:
        assert 0 <= i <= self.N

        return self.bit1.sum(i) + self.bit2.sum(i) * i

    # [l, r)の和, 1-indexed, l=rなら0を返す
    def range_sum(self, l: int, r: int) -> T:
        assert 1 <= l <= r <= self.bit1.N+1

        return self.sum(r-1) - self.sum(l-1)

# https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_G
N, Q = map(int, input().split())
RASQ = RangeAddSumQuery.new(N, 0)

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        RASQ.add(query[1], query[2]+1, query[3])
    else:
        print(RASQ.range_sum(query[1], query[2]+1))
