N = int(input())
ST = [list(input().split()) for _ in range(N)]

previous = dict()

ans = [0, 0]
for i in range(N):
    try: 
        previous[ST[i][0]] == None
    except KeyError:
        previous[ST[i][0]] = 1
        if int(ST[i][1]) > ans[1]:
            ans[0] = i+1
            ans[1] = int(ST[i][1])

print(ans[0])