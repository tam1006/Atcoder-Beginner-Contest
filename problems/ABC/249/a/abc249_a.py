A, B, C, D, E, F, X = map(int, input().split())

takahasi = X//(A+C)*A*B + min((X - X//(A+C)*(A+C)), A)*B
aoki = X//(D+F)*D*E + min((X - X//(D+F)*(D+F)), D)*E

if takahasi > aoki:
    print('Takahashi')
elif takahasi < aoki:
    print('Aoki')
else:
    print('Draw')