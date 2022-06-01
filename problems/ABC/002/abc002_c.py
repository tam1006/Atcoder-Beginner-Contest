ax, ay, bx, by, cx, cy = map(int, input().split())

a = (bx - ax, by - ay)
b = (cx - ax, cy - ay)

print(abs(a[0] * b[1] - a[1] * b[0])/2)