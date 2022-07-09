X = int(input())

ans = 1
for i in range(2, int(X**(1/2))+1):
    p = i
    while p < X:
        p *= i
    
    if p > X:
        p = p // i
    if p > ans and p != i:
        ans = p

print(ans)