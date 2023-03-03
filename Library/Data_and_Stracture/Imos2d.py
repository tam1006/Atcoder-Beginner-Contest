# 二次元いもす法

# 二次元に拡張子たいもす法
# 二次元座標(HxW)において、ある矩形区間にある値vを足すという操作をK回繰り返した結果を、O(K+HW)で求めるアルゴリズム

# 矩形の左上に+v, 右上に-v, 左下に-v, 右下に+vを加算する。
# 最後に縦方向、続いて横方向に累積和を取れば、全体の結果が得られる。

import copy
class Imos2d:
    # H: 配列の高さ
    # W: 配列の幅
    # WARNING: 暗黙的に0始まり、H-1, W-1までの値をとり得るとしていることに注意。負の座標とかの場合は適宜変更
    def __init__(self, H, W):
        self.H = H
        self.W = W
        self.data = [[0] * W for _ in range(H)]

    # [lx, rx) * [ly, ry)にvを加算
    def add(self, lx, rx, ly, ry, v):
        assert 0 <= lx < rx <= self.H
        assert 0 <= ly < ry <= self.W

        self.data[lx][ly] += v
        self.data[lx][ry] -= v
        self.data[rx][ly] -= v
        self.data[rx][ry] += v

    # 累積和を取ることで、全体の結果を得る
    def get(self, new_array=False):
        if new_array:
            result = copy.deepcopy(self.data)
        else:
            result = self.data

        # 横方向に累積和を取る
        for h in range(self.H):
            for w in range(1, self.W):
                result[h][w] += result[h][w - 1]

        # 縦方向に累積和を取る
        for w in range(self.W):
            for h in range(1, self.H):
                result[h][w] += result[h - 1][w]

        return result


# https://atcoder.jp/contests/typical90/tasks/typical90_ab
N = int(input())
imos = Imos2d(1001, 1001)

for _ in range(N):
    # この問題では、グリッドの内部の点を含む矩形を考えてるから、rx+1, ry+1としなくて良い。そのままで半開半閉区間で指定できてる。
    lx, ly, rx, ry = map(int, input().split())
    imos.add(lx, rx, ly, ry, 1)

grid = imos.get()

ans = [0] * (N+1)
for h in range(1001):
    for w in range(1001):
        ans[grid[h][w]] += 1

print(*ans[1:], sep='\n')
