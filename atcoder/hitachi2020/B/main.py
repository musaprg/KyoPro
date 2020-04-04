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
    A,B,M = map(int, input().split())
    aa = list(map(int, input().split()))
    bb = list(map(int, input().split()))
    ans = min(aa) + min(bb)
    for _ in range(M):
        x,y,c = map(int, input().split())
        ans = min(ans, aa[x-1] + bb[y-1] - c)
    print(ans)

if __name__ == '__main__':
    main()
