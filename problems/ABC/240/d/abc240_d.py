from collections import deque
N = int(input())
a = deque(list(map(int, input().split())))

ans = 0
ans_lis = deque()
while a:
    b = a.popleft()
    if len(ans_lis) == 0:
        ans_lis.append([b, 1])
        ans += 1
    elif b == ans_lis[-1][0]:
        ans_lis[-1][1] += 1
        if ans_lis[-1][1] == ans_lis[-1][0]:
            ans -= ans_lis[-1][0] - 1
            ans_lis.pop()
        else:
            ans += 1
    else: 
        ans_lis.append([b, 1])
        ans += 1
        
    print(ans)
