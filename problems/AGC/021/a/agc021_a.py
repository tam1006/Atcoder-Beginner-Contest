N = input()


print(max(sum(int(n) for n in N), int(N[0])-1 + (len(N)-1)*9))