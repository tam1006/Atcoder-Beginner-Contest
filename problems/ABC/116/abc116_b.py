s = int(input())

def f(a):
    if a % 2 == 0:
        return a / 2
    else:
        return 3*a + 1

a = [s]
i = 1
while True:
    i += 1
    a_next = f(a[-1])
    if a_next in a:
        print(i)
        break
    else:
        a.append(a_next)