A, B = map(int, input().split())

min_money = B*10
max_money = (B+1)*10 - 1
for money in range(min_money, max_money+1):
    if int(money*0.08) == A:
        print(money)
        exit()

print(-1)