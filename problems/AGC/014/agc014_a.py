A, B, C = map(int, input().split())

def swap(A, B, C):
    if A == B == C:
        return 0, 0, 0, False
    else:
        return (B+C)/2, (A+C)/2, (A+B)/2, True

if A % 2 != 0 or B % 2 != 0 or C % 2 != 0:
    print(0)
else:
    count = 0
    while True:
        A, B, C, flag = swap(A, B, C)
        if flag:
            count += 1
            if A % 2 != 0 or B % 2 != 0 or C % 2 != 0:
                print(count)
                break
        else:
            print(-1)
            break
