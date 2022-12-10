def solve(S, K):
    for i in range(K):
        if i >= len(S):
            return 1
        if S[i] != '1':
            return int(S[i])

    return 1

def main():
    S = input()
    K = int(input())

    print(solve(S, K))

if __name__ == '__main__':
    main()
