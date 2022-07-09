A, B = map(int, input().split())
S = input()

if S[:A].isdigit() and S[A] == '-' and S[A+1:].isdigit():
    print('Yes')
else:
    print('No')
