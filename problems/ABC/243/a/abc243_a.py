V, A, B, C = map(int, input().split())

while V > 0:
    V -= A
    if V < 0:
        print('F')
        break
    elif V == 0:
        print('M')
        break
    
    V -= B
    if V < 0:
        print('M')
        break
    elif V == 0:
        print('T')
        break
    
    V -= C
    if V < 0:
        print('T')
        break
    elif V == 0:
        print('F')
        break