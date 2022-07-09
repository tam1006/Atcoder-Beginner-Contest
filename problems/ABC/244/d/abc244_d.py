S = input()
T = input()

num = 0
for i in range(3):
    if S[i] != T[i]:
        num += 1

if num % 2 == 1:
    print('No')
else:
    print('Yes')