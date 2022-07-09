time = [int(input()) for _ in range(5)]

last = 0
for i in range(5):
    if time[i] % 10 != 0 and time[i] % 10 < time[last] % 10:
        last = i

ans = time[last]
for i in range(5):
    if i == last:
        continue
    ans += time[i]
    if time[i] % 10 != 0:
        ans += 10 - time[i] % 10

print(ans)