X = int(input())

while X % 100 != 0:
    if X < 100:
        print(0)
        exit()
    
    if X % 100 > 5:
        X -= 105
    else:
        break

print(1)