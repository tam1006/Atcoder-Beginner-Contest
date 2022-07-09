S = input()

ans = [S[0]]

i = 1
while i < len(S):
    if S[i] == ans[-1]:
        if i == len(S)-1:
            break
        ans.append(S[i:i+2])
        i += 2
    else:
        ans.append(S[i])
        i += 1

print(len(ans))