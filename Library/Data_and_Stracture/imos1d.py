# １次元いもす法

# 長さNの1次元配列において、ある連続する区間に、ある数vを足すという操作をK回繰り返した結果を、O(N+K)で求めるアルゴリズム)
# 1次元であれば、セグ木やBITを使ったRAQと同じ。ただ、いもす法は２次元以上に拡張できるのが強み。
# とりあえず1次元

# [l, r)にvを加算したい時、l番目の要素にvを加算、r番目の要素に-vを加算する。
# 最後に累積和を取れば、全体の結果が得られる。


import copy
# 0-indexed
class Imos1d:
    # N: 配列の長さ, 0始まりでN-1までの値をとり得るとする
    def __init__(self, N):
        self.N = N
        self.data = [0] * (N + 1)

    # [l, r)にvを加算
    def add(self, l, r, v):
        assert 0 <= l < r <= self.N

        self.data[l] += v
        self.data[r] -= v

    # 累積和を取ることで、全体の結果を得る
    def get(self, new_array=False):
        if new_array:
            result = copy.deepcopy(self.data)
        else:
            result = self.data

        for i in range(1, self.N):
            result[i] = result[i - 1] + self.data[i]

        return result[:self.N]

# https://atcoder.jp/contests/abc014/tasks/abc014_3
N = int(input())
imos = Imos1d(10 ** 6 + 1)

for _ in range(N):
    l, r = map(int, input().split())
    imos.add(l, r + 1, 1)

ans = imos.get()
print(max(ans))
