N = int(input())
T = input()

direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]
num = 0
zahyo = [0, 0]

for i in range(len(T)):
    if T[i] == 'R':
        num += 1
        num %= 4
    else:
        zahyo[0] += direction[num][0]
        zahyo[1] += direction[num][1]
    # print(zahyo)

print(f'{zahyo[0]} {zahyo[1]}')