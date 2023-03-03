# 閉路探索

## 有向グラフ トポロジカルソート

# edges: 隣接リスト
def topological_sort(edges):
    from collections import deque

    N = len(edges)
    inc = [0] * N # 入次数
    out = [[] for _ in range(N)] # 出次ノードリスト

    deq = [i for i, _ in enumerate(inc) if inc[i] == 0] # 入次数0のノード集合
    deq = deque(deq)
    L = [] # トポロジカルソート結果

    if len(deq) == 0:
        print("閉路が存在します")
        return

    while deq:
        n = deq.popleft()
        L.append(n)
        for m in out[n]:
            inc[m] -= 1
            if inc[m] == 0:
                deq.append(m)

    if len(L) != N:
        print("閉路が存在します")
        return

    return L




