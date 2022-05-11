S = input()

S = sorted(S)
ans = 'a'

i = 0
while True:
    if i >= len(S):
        if ans == chr(ord('z')+1):
            ans = 'None'
        break
    elif ord(ans) >= ord(S[i]):
        ans = chr(ord(S[i]) + 1)
        i += 1
    else:
        break

print(ans)