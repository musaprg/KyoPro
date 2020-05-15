import sys
from collections import defaultdict, Counter, deque
from itertools import accumulate, permutations, combinations
from operator import itemgetter
from bisect import bisect_left, bisect_right, bisect
from heapq import heappop, heappush
from fractions import gcd
from math import ceil, floor, sqrt, cos, sin, pi
from copy import deepcopy

# If you use recursive call, uncomment this code
#sys.setrecursionlimit(10**6)

def main():
    n = int(input())
    kukan = [(n,0,n-1)]
    a = [0]*n
    i = 1
    while len(kukan) != 0 and i <= n:
        _,l,r = heappop(kukan)
        if l > r:
            continue
        if l == r:
            a[l] = i
        else:
            m = (l+r)//2
            a[m] = i
            if 0 <= m-1:
                heappush(kukan, (-1*(m-l),l,m-1))
            if m+1 < n:
                heappush(kukan, (-1*(r-m),m+1,r))
        i += 1
    return " ".join(map(str, a))

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        print(main())
