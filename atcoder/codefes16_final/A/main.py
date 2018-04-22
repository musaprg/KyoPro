import sys

h,w = map(int, input().split(" "))
xnames = [chr(x) for x in range(ord("A"),ord("A")+w+1)]
ynames = [x for x in range(1,h+1)]
for y in range(h):
    for x in range(w):
        s = input()
        if s == "snuke":
            print(xnames[x]+ynames[y])
            sys.exit(0)



