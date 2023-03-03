N, K = map(int, input().split())
a = list(map(int, input().split()))


from collections import deque
from collections import defaultdict
ans = 0

que = deque([])
count = defaultdict(int)
identical = 0
i = 0

while i < N:
    if count[a[i]] != 0:
        que.append(a[i])
        count[a[i]] += 1
    elif identical < K:
        que.append(a[i])
        count[a[i]] += 1
        identical += 1
    else:
        while que:
            q = que.popleft()
            count[q] -= 1
            if count[q] == 0:
                break

        que.append(a[i])
        count[a[i]] += 1

    ans = max(ans, len(que))
    i += 1

print(ans)


