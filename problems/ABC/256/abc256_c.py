h1, h2, h3, w1, w2, w3 = map(int, input().split())

H = h1 + h2 + h3
W = w1 + w2 + w3
if H != W:
    print(0)
    exit()

A = H
ans = 0
for a11 in range(1, A+1):
    for a13 in range(1, A+1):
        if a11+a13 > A:
            continue
        for a33 in range(1, A+1):
            if a11+a13+a33 > A:
                continue
            for a31 in range(1, A+1):
                if a11+a13+a33+a31 > A:
                    continue

                a12 = h1 - a11 - a13
                a21 = w1 - a11 - a31
                a32 = h3 - a31 - a33
                a23 = w3 - a13 - a33
                a22 = w2 - a12 - a32

                if a12 > 0 and a21 > 0 and a32 > 0 and a23 > 0 and a22 > 0 and (a11+a12+a13+a21+a22+a23+a31+a32+a33 == A):
                    ans += 1

print(ans)