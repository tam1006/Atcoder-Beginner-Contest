N = int(input())

if N % 2 == 1:
    print()
    exit()

ans = []
for i in range(1<<N):
    tmp = ''
    for j in range(N):
        if i & (1<<j):
            tmp += '('
        else:
            tmp += ')'

    if tmp.count('(') != tmp.count(')'):
        continue

    left = 0
    flag = True
    for j in range(N):
        if tmp[j] == '(':
            left += 1
        else:
            left -= 1

        if left < 0:
            flag = False
            break

    if flag:
        ans.append(tmp)

ans = sorted(ans)
for i in range(len(ans)):
    print(ans[i])
