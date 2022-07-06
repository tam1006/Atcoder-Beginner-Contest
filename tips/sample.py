with open('test.txt', 'w') as f:
    for i in range(3000):
        print('1'*3000, file=f)