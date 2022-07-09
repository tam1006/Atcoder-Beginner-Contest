S = input()

Omojiflag = False
Komojiflag = False
moji = []

for s in S:
    uni = ord(s)
    moji.append(uni)

    if uni < ord('Z'):
        Omojiflag = True
    
    if uni >= ord('Z'):
        Komojiflag = True

if len(set(moji)) == len(list(S)) and Omojiflag and Komojiflag:
    print('Yes')
else:
    print('No')