S = input()
T = input()

flag = True
i = 0
j = 0
while i < len(S):
    if j >= len(T):
        flag = False
        break

    if S[i] == T[j]:
        i += 1
        j += 1
    elif i == 0 or i == 1:
        flag = False
        break
    elif S[i-1] == S[i-2] and T[j] == S[i-1]:
        moji = T[j]
        while T[j] == moji:
            j += 1
            if j == len(T):
                flag = False
                break
    else:
        flag = False
        break

if flag:
    print('Yes')
else:
    print('No')