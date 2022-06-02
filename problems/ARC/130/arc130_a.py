N = int(input())
S = input()

def nC2(n):
    return n*(n-1)//2

ans = 0
i = 0
while i < N-1:
    tmp = 0
    if S[i] == S[i+1]:
        while S[i] == S[i+1]:
            tmp += 1
            i += 1
            if i == N-1:
                break
        ans += nC2(tmp+1)
    i += 1

print(ans)