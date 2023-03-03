# Binaray Indexed Tree BIT

from typing import TypeVar, Callable, List
T = TypeVar('T')

# [l, r)の和, l=rなら0を返す O(logN)
# i番目の値をxに変更する O(logN)
# 1-indexed
class RangeSumQuery:
    def __init__(self, data: List[T], identity: T):
        self.data = data
        self.identity = identity
        self.N = len(data) - 1

    # 初期値を配列Aで初期化, 全てidentityの値からの実行
    @classmethod
    def from_list(cls, A: List[T], identity: T):
        data = [identity] * (len(A) + 1)
        self = cls(data, identity)
        for i in range(len(A)):
            self.add(i+1, A[i])
        return self

    @classmethod
    def new(cls, size: int, identity: T):
        data = [identity] * (size + 1)
        return cls(data, identity)

    # i番目の値にxを加算する
    def add(self, i: int, x: T):
        assert 1 <= i <= self.N

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

# https://atcoder.jp/contests/practice2/tasks/practice2_b
# https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_B
import sys
input = lambda: sys.stdin.readline().rstrip()

N, Q = map(int, input().split())
# a = list(map(int, input().split()))

# bit = RangeSumQuery.from_list(a, 0)
bit = RangeSumQuery.new(N, 0)

for _ in range(Q):
    # 0-indexed
    t, a, b = map(int, input().split())
    if t == 0:
        p = a
        x = b

        bit.add(p, x)
    else:
        l = a
        r = b

        print(bit.range_sum(l, r+1))
