S = input()
S = S[::-1]
temp = [0]*len(S)
for i in range(len(S)):
    if S[i] == str(6):
        temp[i] = 9
    elif S[i] == str(9):
        temp[i] = 6
    else:
        temp[i] = int(S[i])

ans = ""
for i in range(len(S)):
    ans += str(temp[i])

print(ans)