import os

alphabets = [chr(i) for i in range(ord('a'), ord('z') + 1)]
for a in alphabets:
    if a in ['a', 'b']:
        for b in alphabets:
            os.makedirs(f"{a}{b}", exist_ok=True)
            problem = f"{a}{b}/typical90_{a}{b}"
            with open(f"{problem}.py", "w") as f:
                pass

    elif a == 'c':
        for b in [chr(i) for i in range(ord('a'), ord('l') + 1)]:
            os.makedirs(f"{a}{b}", exist_ok=True)
            problem = f"{a}{b}/typical90_{a}{b}"
            with open(f"{problem}.py", "w") as f:
                pass
    os.makedirs(f"{a}", exist_ok=True)
    problem = f"{a}/typical90_{a}"
    with open(f"{problem}.py", "w") as f:
        pass
