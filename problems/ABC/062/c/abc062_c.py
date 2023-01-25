def solve(H, W):
    ans = float('inf')

    for h in range(1, H):
        s1 = h*W
        s2w = (H-h)*(W//2)
        s3w = (H-h)*(W-W//2)

        s2h = ((H-h)//2)*W
        s3h = ((H-h)-(H-h)//2)*W

        ans = min(ans, max(s1, s2w, s3w) - min(s1, s2w, s3w))
        ans = min(ans, max(s1, s2h, s3h) - min(s1, s2h, s3h))

    for w in range(1, W):
        s1 = H*w
        s2h = (W-w)*(H//2)
        s3h = (W-w)*(H-H//2)

        s2w = ((W-w)//2)*H
        s3w = ((W-w)-(W-w)//2)*H

        ans = min(ans, max(s1, s2h, s3h) - min(s1, s2h, s3h))
        ans = min(ans, max(s1, s2w, s3w) - min(s1, s2w, s3w))

    return ans


def main():
    H, W = map(int, input().split())
    print(solve(H, W))

if __name__ == '__main__':
    main()
