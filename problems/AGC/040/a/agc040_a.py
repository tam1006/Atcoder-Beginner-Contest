import numpy as np

S = input()

ans = [0]*(len(S)+1)
ans = np.array(ans)
zero_max = [0, 0]
for i in range(1, len(S)+1):
    if i == len(S):
        if S[i-1] == '>':
            ans[i] = ans[i-1] - 1
            diff = ans[i]
            if diff < 0:
                ans[zero_max[1]:] -= diff
        else:
            ans[i] = ans[i-1] + 1
        continue

    if S[i-1] == '>' and S[i] == '<':
        ans[i] = ans[i-1] - 1
        zero_max[0] = i
        diff = ans[i]
        if diff < 0:
            ans[zero_max[1]:i+1] -= diff
        elif diff > 0:
            ans[zero_max[1]+1:i+1] -= diff
    elif S[i-1] == '<' and S[i] == '>':
        ans[i] = ans[i-1] + 1
        zero_max[1] = i
    elif S[i-1] == '<':
        ans[i] = ans[i-1] + 1
    else:
        ans[i] = ans[i-1] - 1

print(sum(ans))