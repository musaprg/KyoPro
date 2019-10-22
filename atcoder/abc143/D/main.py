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

def reverse_bisect(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x > a[mid]: hi = mid
        else: lo = mid+1
    return lo

def main():
    N = int(input())
    ll = list(map(int,input().split()))
    ll = sorted(ll)

    ans = 0

    for i in range(N-1,-1,-1):
        a = ll[i] # 長辺
        for bidx in range(i-1,-1,-1):
            b = ll[bidx] # 適当に一つ決める
            #cidx = bisect_right(ll[:bidx],a-b) # a-b<cを満たすcを二分探索で探す
            cidx = reverse_bisect(ll[:bidx],a-b)
            print(ll[:bidx])
            print(cidx)
            for c in ll[:cidx]:
                print("check:",a,b,c)
                if (b<a+c) and (c<a+b):
                    print("passed")
                    ans += 1

    print(ans)

if __name__ == '__main__':
    main()
