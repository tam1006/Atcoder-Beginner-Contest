N = int(input())
A = list(map(int, input().split()))

from collections import defaultdict

#nの約数を全て求める
def divisor(n): 
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            if i != 1:
                table.append(i)
            if n//i != i:
                table.append(n//i)
        i += 1
    table = list(set(table))
    return table

dic = defaultdict(int)

for a in A:
    for d in divisor(a):
        dic[d] += 1

print(max(dic.items(), key=lambda x: x[1])[0])