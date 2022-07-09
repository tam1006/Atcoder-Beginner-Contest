a, b, c = map(int, input().split())

s = [a, b, c]
s.sort()


if b == s[1]:
    print('Yes')
else:
    print('No')