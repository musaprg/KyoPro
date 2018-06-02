s, c, n = map(int, input().split(" "))
K = input()
for k in K:
    if k == "S" and s != 0:
        s -= 1
    elif k == "C" and c != 0:
        c -= 1
    elif k == "E":
        if s == 0 and c == 0:
            continue
        else:
            if s >= c:
                s -= 1
            elif c != 0:
                c -= 1
print(s)
print(c)