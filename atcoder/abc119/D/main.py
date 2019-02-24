import bisect
import sys

def solve(ss,tt,x):
    si = bisect.bisect(ss,x)
    ti = bisect.bisect(tt,x)
    sleft, sright = fidx(ss,si)
    tleft, tright = fidx(tt,ti)
    print(sleft, " ", sright)
    print(tleft, " ", tright)
    

def fidx(ss, si):
    s = [None]*2

    if si >= 0 and si <= (len(ss)-1):
        s[0] = ss[si]
    elif si == len(ss):
        s[0] = ss[si-1]
    else:
        s[0] = -sys.maxsize
    
    if s[0] == -sys.maxsize:
        if s[0] < len(ss):
            s[1] = ss[si+1]
        else:
            s[1] = sys.maxsize
    else:
        if si+1 == len(ss):
            s[1] = sys.maxsize
        else:
            s[1] = ss[si+1]

    return s[0], s[1]


def main():
    A,B,Q = map(int,input().split())
    ss = []
    tt = []
    for i in range(A):
        s = int(input())
        ss.append(s)
    for i in range(B):
        t = int(input())
        tt.append(t)
    ss.sort()
    tt.sort()
    for i in range(Q):
        x = int(input())
        print(solve(ss,tt,x))


if __name__ == '__main__':
    main()
