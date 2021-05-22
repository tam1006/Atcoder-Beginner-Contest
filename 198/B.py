N = str(input())

N = N[::-1]
count = 0

for i in range(len(N)):
    if N[i] == str(0):
        count += 1
    else:
        break

N = N[i:]
N_rev = N[::-1]

if N == N_rev:
    print("Yes")
else:
    print("No")