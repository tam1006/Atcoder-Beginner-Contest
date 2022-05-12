antena = [int(input()) for _ in range(5)]
k = int(input())

if max(antena) - min(antena) <= k:
    print('Yay!')
else:
    print(':(')