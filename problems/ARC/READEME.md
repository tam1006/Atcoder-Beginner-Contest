# AtcoderのABC問題のリポジトリです

## グラフ問題の入力の受け方
N, M = map(int, input().split())  
g = [[]*N for i in range(N)]  
for i in range(M):  
    u, v = map(int, input().split())  
    u -= 1  
    v -= 1  
    g[u].append(v)  
    g[v].append(u)  

これでgのインデックスに、繋がっている頂点が格納される。

## popとpush
from collections import deque  

d = deque([1, 2, 3])  
d.append(4)  
->[1,2,3,4]   
d.appendleft(0)  
->[0,1,2,3,4]  
a = d.pop()  
->[0,1,2,3]  
b = d.popleft()  
->[1,2,3]  
collectionはO(1)で計算できる