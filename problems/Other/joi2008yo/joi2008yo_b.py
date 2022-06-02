s = input()

JOI = 0
IOI = 0
for i in range(len(s)-2):
    if s[i:i+3] == 'JOI':
        JOI += 1
    elif s[i:i+3] == 'IOI':
        IOI += 1

print(JOI)
print(IOI)