def is_tasai(s) -> bool:
    return len(s) == len(set(s))

def get_alphabets():
    alphabets = []
    for i in range(ord("a"), ord("z")+1):
        alphabets.append(chr(i))
    return alphabets

def next(s):
    

def solve(s) -> str:
    nexts = None
    while True:
        nexts = next(s)
        if is_tasai(nexts):
            return nexts
    if len(nexts) >= 27:
        return "-1"
    else:
        return nexts

if __name__ == '__main__':
    s = input()
    if len(s) == 26 and is_tasai(s):
        print(-1)
    else:
        print(solve(s))