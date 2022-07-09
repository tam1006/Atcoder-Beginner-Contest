X, Y = map(int, input().split())
import math

if X >= Y:
    print(0)
else:
    print(math.ceil((Y-X)/10))
