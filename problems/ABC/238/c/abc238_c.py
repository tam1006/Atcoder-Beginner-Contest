N = int(input())
CONST = 998244353

def f(x):
    return (x - (10*(len(str(x))-1) - 1)) % CONST

if len(str(N)) == 1:
    print()

for i in range(len(str(N))):
