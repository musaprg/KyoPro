from collections import defaultdict

def main():
    while True:
        n,m,a = map(int,input().split())
        if not n and not m and not a:
            return
        hlines = [tuple(map(int,input().split())) for _ in range(m)]
        hlines = sorted(hlines, key=lambda x: x[0], reverse=True)

        for h in range(hlines[0][0], -1, -1):
            for hline in hlines:
                if hline[0] == h:
                    if hline[1] == a:
                        a = hline[2]
                    elif hline[2] == a:
                        a = hline[1]

        print(a)

if __name__ == '__main__':
    main()
