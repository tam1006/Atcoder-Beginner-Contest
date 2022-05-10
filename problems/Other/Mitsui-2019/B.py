import math
N = int(input())

if ((N+1)/1.08 > math.ceil(N/1.08)):
    print(math.ceil(N/1.08))
else:
    print(":(")