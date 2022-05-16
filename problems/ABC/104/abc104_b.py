
S = input()

if S[0] != 'A':
    print('WA')
    exit()

cnt = 0
ind = None
for i in range(2, len(S)-1):
    if S[i] == 'C':
        cnt += 1
        ind = i

if cnt != 1:
    print('WA')
    exit()

string = S[1:ind] + S[ind+1:]
if string.lower() != string:
    print('WA')
    exit()

print('AC')