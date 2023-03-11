# Sliding Window

# 長さNの配列の、連続するK個の要素の和の最小値を、全ての連続するK個の要素について求める問題
# RMQを使うとO(NlogN)で解けるが、Sliding Windowを使うとO(N)で解ける
# dequeで実装する。詳しくは蟻本P301

# N: 配列の長さ
# K: 連続する要素の数, 1 <= k <= n
# A: 配列
def sliding_window(N, K, A):
    from collections import deque

    # dequeには配列aのインデックスを格納していく
    deq = deque()

    for i in range(K-1):
        # a[i]がdeqの末尾よりも大きい限り、末尾をpopする
        # これによって、deqの末尾は常に最小の要素を指す
        while deq and A[deq[-1]] >= A[i]:
            deq.pop()
        deq.append(i)

    ans = []
    for i in range(K-1, N):
        while deq and A[deq[-1]] >= A[i]:
            deq.pop()

        deq.append(i)

        ans.append(A[deq[0]])

        if deq and deq[0] == i - K + 1:
            deq.popleft()

    return ans

# https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/3/DSL_3_D

N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = sliding_window(N, K, A)
print(*ans)
