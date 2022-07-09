O = input()
E = input()

password = []
for i in range(len(E)):
    password.append(O[i] + E[i])

if len(O) > len(E):
    password.append(O[-1])

print(''.join(password))