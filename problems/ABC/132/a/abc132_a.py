S = input()

dic = dict()
for i in S:
    if not i in dic:
        dic[i] = 1
    else:
        dic[i] += 1

if all(dic[i] == 2 for i in dic):
    print("Yes")
else:
    print("No")