a, b = map(int, input().split())

if a > 0:
    print('Positive')
elif a <= 0:
    if b >= 0:
        print('Zero')
    else:
        if (-a-b-1)%2 == 0:
            print('Positive')
        else:
            print('Negative')
