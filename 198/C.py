r, x, y = map(int, input().split())

distance = (x**2+y**2)**(1/2)

if distance // r == 0:
    print(2)
elif distance % r == 0:
    print(int(distance//r))
else:
    print(int(distance//r+1))