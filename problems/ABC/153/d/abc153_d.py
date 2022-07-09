H = int(input())

num = 1

while H > 0:
    if H == 1:
        num *= 2
        break
    else:
        num *= 2
        H = int(H/2)

print(num-1)



