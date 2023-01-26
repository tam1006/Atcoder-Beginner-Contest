def solve():
    global S1, S2, S3, alphabet
    alphabet = set()
    for s in [S1, S2, S3]:
        for c in s:
            alphabet.add(c)

    if len(alphabet) > 10:
        return ['UNSOLVABLE']


    global ans
    ans = ['UNSOLVABLE']

    dfs(0, [-1]*len(alphabet), [False]*10)

    return ans



def dfs(i, nums, used):
    global S1, S2, S3, alphabet, ans
    if i == len(alphabet):
        flag, c = check(nums)
        if flag:
            ans = c
            return True
        return False

    for j in range(10):
        if not used[j]:
            used[j] = True
            nums[i] = j
            if dfs(i+1, nums, used):
                return True
            used[j] = False
            nums[i] = -1

    return False

def check(nums):
    global S1, S2, S3, alphabet

    d = {}
    for i, c in enumerate(alphabet):
        d[c] = nums[i]

    if d[S1[0]] == 0 or d[S2[0]] == 0 or d[S3[0]] == 0:
        return False, []

    n1 = 0
    for c in S1:
        n1 = n1*10 + d[c]

    n2 = 0
    for c in S2:
        n2 = n2*10 + d[c]

    n3 = 0
    for c in S3:
        n3 = n3*10 + d[c]

    flag = n1 + n2 == n3
    return flag, [n1, n2, n3]


def main():
    global S1, S2, S3
    S1 = input()
    S2 = input()
    S3 = input()
    ans = solve()

    for a in ans:
        print(a)

if __name__ == '__main__':
    main()
