S = input()

A = -1
Z = -1
for i in range(len(S)):
    if S[i] == 'A':
        A = i
        break

for i in range(len(S)-1, -1, -1):
    if S[i] == 'Z':
        Z = i
        break


print(Z-A+1)