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

A = None
B = None
N = None

def calc(x):
    return floor(A*x/B) - A * floor(x/B)

def main():
    global A,B,N
    A,B,N = map(int, input().split())
    if B > N:
        return calc(N)
    else:
        #mmax = 0
        #for x in range(N+1):
        #    mmax = max(mmax, calc(x))
        #print(mmax)
        return calc(B-1)

if __name__ == '__main__':
    print(main())
