n = int(input())
num = list(int(input()) for _ in range(n))

taro = []
hanako = []
for i in range(1, 2*n+1):
    if i in num:
        taro.append(i)
    else:
        hanako.append(i)

taro.sort()
hanako.sort()
now = 0
while len(taro) > 0 and len(hanako) > 0:
    if taro[-1] > now:
        for i in range(len(taro)):
            if taro[i] > now:
                now = taro.pop(i)
                flag = False
                break
    else:
        now = 0
    
    if len(taro) == 0:
        break
    
    if hanako[-1] > now:
        for i in range(len(hanako)):
            if hanako[i] > now:
                now = hanako.pop(i)
                break
    else:
        now = 0

print(len(hanako))
print(len(taro))