S = input()

from collections import Counter

if len(S) == 1:
    if S == '8':
        print('Yes')
    else:
        print('No')
    exit()
elif len(S) == 2:
    if int(S) % 8 == 0 or int(S[::-1]) % 8 == 0:
        print('Yes')
    else:
        print('No')
    exit()

c = Counter(S)

for i in range(8, 1001, 8):
    num = str(format(i, '03d'))
    eight = Counter(num)
    flag = True
    for k, v in eight.items():
        if c[k] < v:
            flag = False
            break
    
    if flag:
        print('Yes')
        exit()

print("No")