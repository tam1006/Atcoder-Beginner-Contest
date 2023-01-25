import heapq

def solve(N, a):
    forward = a[:N]
    backward = [-a[2*N+i] for i in range(N)]

    heapq.heapify(forward)
    heapq.heapify(backward)

    S_f = [sum(forward)]
    S_b = [-sum(backward)]

    for i in range(N):
        heapq.heappush(forward, a[N+i])
        min_forward = heapq.heappop(forward)

        if min_forward == a[N+i]:
            S_f.append(S_f[-1])
        else:
            S_f.append(S_f[-1] - min_forward + a[N+i])

        heapq.heappush(backward, -a[2*N-i-1])
        max_backward = -heapq.heappop(backward)

        if max_backward == a[2*N-i-1]:
            S_b.append(S_b[-1])
        else:
            S_b.append(S_b[-1] - max_backward + a[2*N-i-1])

    ans = -float('inf')
    for i in range(N+1):
        ans = max(ans, S_f[i] - S_b[-1-i])

    return ans



def main():
    N = int(input())
    a = list(map(int, input().split()))
    print(solve(N, a))

if __name__ == '__main__':
    main()
