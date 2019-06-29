import itertools

def main():
    n = int(input())
    for _ in range(n):
        s = input()
        ssum = set()
        for i in range(len(s)):
            l = s[:i]
            rl = l[::-1]
            r = s[i:]
            rr = r[::-1]
            ssum.add(l+r)
            ssum.add(r+l)
            ssum.add(rl+r)
            ssum.add(r+rl)
            ssum.add(l+rr)
            ssum.add(rr+l)
            ssum.add(rl+rr)
            ssum.add(rr+rl)
        print(len(ssum))

if __name__ == '__main__':
    main()
