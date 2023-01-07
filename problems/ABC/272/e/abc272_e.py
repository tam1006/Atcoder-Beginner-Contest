import math

# def solve(N: int, M: int, A: List[int]) -> List[str]:
def solve(N, M, A):
    nums = list(set() for _ in range(M+1))

    for i in range(N):
        j = max(1, math.ceil(-A[i]/(i+1)))
        for k in range(j, M+1):
            num = A[i] + k*(i+1)
            if num > N:
                break
            nums[k].add(num)

    ans = []
    for i in range(1, M+1):
        for j in range(N+1):
            if j not in nums[i]:
                ans.append(j)
                break

    return ans

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    M = int(next(tokens))
    A = [None for _ in range(N)]
    for i in range(N):
        A[i] = int(next(tokens))
    assert next(tokens, None) is None

    ans = solve(N, M, A)
    for i in range(M):
        print(ans[i])

if __name__ == '__main__':
    main()
