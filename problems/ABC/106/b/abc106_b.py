N = int(input())

#nの約数を全て求める
def divisor(n): 
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table

num = 0
for i in range(1, N+1, 2):
    div = divisor(i)
    if len(div) == 8:
        num += 1

print(num)