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
    N = int(input())
    t = (N-1)//2
    ans = 0
    for i in range(0,t):
        ans += (i+1) * 8 * (i+1)
    return ans

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        print(main())
