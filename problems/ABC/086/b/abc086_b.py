a, b = map(int, input().split())

num = int(str(a)+str(b))

if (num ** (1/2)).is_integer():
    print('Yes')
else:
    print('No')