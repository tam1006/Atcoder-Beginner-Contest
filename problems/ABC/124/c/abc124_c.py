
S = list(input())
# S = [int(i) for i in S]

# b = [0, 1]*(len(S)//2) + [0]*(1 if len(S)%2 else 0)
# w = [1, 0]*(len(S)//2) + [1]*(1 if len(S)%2 else 0)

b = 0
w = 0
for i in range(len(S)):
    if i % 2 == 0:
        if S[i] == '0':
            w += 1
        else:
            b += 1
    else:
        if S[i] == '1':
            w += 1
        else:
            b += 1

print(min(b, w))