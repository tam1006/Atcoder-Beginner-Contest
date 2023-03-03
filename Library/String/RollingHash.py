# Rolling Hash

# 文字列Sが与えられた時に、その区間[l1, r1)と[l2, r2)が一致するかの判定ができる。

# 2^61 - 1 をmodとしたRolling Hash
# https://qiita.com/keymoon/items/11fac5627672a6d6a9f6
class RollingHash_61:
    def __init__(self, S):
        self.MASK30 = (1 << 30) - 1
        self.MASK31 = (1 << 31) - 1
        self.MASK61 = (1 << 61) - 1
        self.POSITIVIZER = self.MASK61 * ((1 << 3) - 1)

        # 文字列Sを整数に変換する
        S = [ord(i) for i in S]
        l = len(S)
        self.base = 37
        self.mod = self.MASK61
        self.pow = [1]*(l+1)

        # 区間[0, i)のハッシュ値を計算しておく
        # 任意区間[l, r) = [0, r) - [0, l)
        self.hash = [0]*(l+1)
        for i in range(l):
            self.pow[i+1] = self.calcMod(self.mul(self.pow[i], self.base))
            self.hash[i+1] = self.calcMod(self.mul(self.hash[i], self.base) + S[i])

    def mul(self, a, b):
        ua = a >> 31
        da = a & self.MASK31
        ub = b >> 31
        db = b & self.MASK31

        mid = da * ub + ua * db
        umid = mid >> 30
        dmid = mid & self.MASK30

        return ua * ub * 2 + umid + (dmid << 31) + da * db


    def calcMod(self, x):
        xu = x >> 61
        xd = x & self.MASK61
        res = xu + xd
        if res >= self.mod:
            res -= self.mod
        return res
        

    def get(self, l, r):
        # 区間[l,r)のハッシュ値を返す
        return self.calcMod(self.hash[r] + self.POSITIVIZER - self.mul(self.hash[l], self.pow[r-l]))

    def is_same(self, l1, r1, l2, r2):
        # 2つの区間[l1,r1)と[l2,r2)のハッシュ値を比較。同じであれば一致
        if (r1 - l1) == (r2 - l2) and self.get(l1, r1) == self.get(l2, r2):
            return True
        else:
            return False

    # 2つの区間[l1,r1)と[l2,r2)の最長共通接頭辞を二部探索で求める
    def lcp(self, l1, r1, l2, r2):
        assert 0 <= l1 < r1 <= len(self.hash)
        assert 0 <= l2 < r2 <= len(self.hash)

        ok = 0
        ng = min(r1-l1, r2-l2) + 1
        while ng - ok > 1:
            mid = (ok + ng) // 2
            if self.is_same(l1, l1+mid, l2, l2+mid):
                ok = mid
            else:
                ng = mid

        return ok


class RollingHash2:
    def __init__(self, S) -> None:
        """文字列->整数変換と2つの基数でのhash生成"""
        S = [ord(i)-96 for i in S]
        l = len(S)
        self.base1 = 10**5+7
        self.base2 = 10**3+7
        self.mod = (1<<31)-1
        self.pow1 = [1]*(l+1)
        self.pow2 = [1]*(l+1)
        self.hash1 = [0]*(l+1)
        self.hash2 = [0]*(l+1)
        for i in range(l):
            self.pow1[i+1] = (self.pow1[i]*self.base1)%self.mod
            self.pow2[i+1] = (self.pow2[i]*self.base2)%self.mod
            self.hash1[i+1] = (self.hash1[i]*self.base1+S[i])%self.mod
            self.hash2[i+1] = (self.hash2[i]*self.base2+S[i])%self.mod
    def gethash(self,l,r):
        """2つの基数でのハッシュ値を返す"""
        a = (self.hash1[r]-self.hash1[l]*self.pow1[r-l])%self.mod
        b = (self.hash2[r]-self.hash2[l]*self.pow2[r-l])%self.mod
        return a, b
    
    def is_same(self, l1, r1, l2, r2):
        """2つの区間[l1,r1)と[l2,r2)の２つの基数でのハッシュ値が一致すればok"""
        a1, b1 = self.gethash(l1, r1)
        a2, b2 = self.gethash(l2, r2)
        if (a1==a2) and (b1==b2):
            return True
        else:
            return False


# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_14_B
# T = input()
# P = input()

# rh_T = RollingHash_61(T)
# rh_P = RollingHash_61(P)

# for i in range(len(T)-len(P)+1):
    # if rh_T.get(i, i+len(P)) == rh_P.get(0, len(P)):
        # print(i)


# https://judge.yosupo.jp/problem/zalgorithm
S = input()
rh = RollingHash_61(S)
ans = []
for i in range(len(S)):
    ans.append(rh.lcp(0, len(S), i, len(S)))

print(*ans)

