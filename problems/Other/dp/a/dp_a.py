def solve(N, h):
    dp = [float('inf')] * (N+1)
    dp[0] = 0
    dp[1] = 0

    h = [h[0]] + h

    for i in range(2, N+1):
        dp[i] = min(dp[i-1] + abs(h[i] - h[i-1]), dp[i-2] + abs(h[i] - h[i-2]))

    return dp[N]

def main():
    N = int(input())
    h = list(map(int, input().split()))

    print(solve(N, h))

if __name__ == '__main__':
    main()
