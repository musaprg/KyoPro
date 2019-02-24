import bisect
import sys

def solve(chk,ll):
    chk.sort()
    ll.sort()
    print(chk)
    print(ll)
    ans = 0
    for c in chk:
        i = bisect.bisect(ll,c)
        c1 = sys.maxsize
        c2 = sys.maxsize
        c3 = sys.maxsize

        c1 = abs(c - ll[i-1])
        if i < len(ll):
            c2 = abs(c - ll[i])
        #c3 = inner(ll[0:i], 0, c)
        ans += min(c1,c2,c3)
    return ans
    
def main():
    N,A,B,C = map(int, input().split())
    chk = [A,B,C]
    ll = []
    for i in range(N):
        l = int(input())
        if l in chk:
            chk.remove(l)
        else:
            ll.append(l)
    if chk:
        return solve(chk,ll)
    else:
        return 0

if __name__ == '__main__':
    print(main())
