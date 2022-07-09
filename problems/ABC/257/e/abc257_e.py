N = int(input())
C = list(map(int, input().split()))

rate = []
x = 0
for i in range(9):
    rate.append([(i+1)/C[i], i])

rate.sort(key=lambda x: x[0], reverse=True)

j = 0
while j < 9:
    if N - C[rate[j][1]] >= 0:
        N -= C[rate[j][1]]
        x = 10*x + rate[j][1] + 1
    else:
        j += 1

print(x)