import math
import bisect

N = int(input())
X, Y = [], []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)


ans = 0.0

def to_arg(theta):
    if theta > 180:
        theta = 360 - theta

    return theta

for j in range(N):
    Ox, Oy = X[j], Y[j]

    def argument_sort(x, y):
        args = []
        for i in range(N):
            if i != j:
                arg = math.atan2(y[i] - Oy, x[i] - Ox)
                if arg < 0:
                    arg += math.pi * 2
                args.append(math.degrees(arg))

        return sorted(args)

    args = argument_sort(X, Y)

    for i in range(N-1):
        if args[i] >= 180:
            index = bisect.bisect_left(args, args[i] - 180)
        else:
            index = bisect.bisect_left(args, args[i] + 180)

        if index == N-1 or index == 0:
            arg1 = to_arg(abs(args[-1] - args[i]))
            arg2 = to_arg(abs(args[i] - args[0]))

            ans = max(ans, arg1, arg2)
        else:
            arg1 = to_arg(abs(args[index] - args[i]))
            arg2 = to_arg(abs(args[i] - args[index-1]))

            ans = max(ans, arg1, arg2)

print(ans)
