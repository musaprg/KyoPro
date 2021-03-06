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
    N,M = map(int, input().split())
    if N == 1:
        return 0
    numtri = (N-1)//2
    remain = (N-1)%2
    ans = 0
    if numtri:
        ans += (M//numtri)*numtri*2
        ans += (M%numtri)*2
    else:
        ans = M
    return ans
        
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        print(main())
