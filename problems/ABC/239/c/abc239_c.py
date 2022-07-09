x1, y1, x2, y2 = map(int, input().split())

def has_duplicates(seq):
    return len(seq) != len(set(seq))

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]
zahyo = []
for i in range(8):
    zahyo.append((x1 + dx[i], y1 + dy[i]))
    zahyo.append((x2 + dx[i], y2 + dy[i]))


if has_duplicates(zahyo):
    print('Yes')
else:
    print("No")