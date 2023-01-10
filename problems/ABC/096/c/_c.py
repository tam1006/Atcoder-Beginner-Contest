#!/usr/bin/env python3
# from typing import *


# def solve(n: int, a: List[int]) -> Any:
def solve(H, W, maze):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for i in range(H):
        for j in range(W):
            if maze[i][j] == '#':
                flag = False
                for sx, sy in zip(dx, dy):
                    ni = i + sx
                    nj = j + sy
                    if 0 <= ni < H and 0 <= nj < W and maze[ni][nj] == '#':
                        flag = True

                if not flag:
                    return 'No'

    return 'Yes'

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    H, W = map(int, input().split())
    maze = [list(input()) for _ in range(H)]

    ans = solve(H, W, maze)

    print(ans)


if __name__ == '__main__':
    main()
