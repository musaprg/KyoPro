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
    pp = list(map(int, input().split()))

    c = 0
    for p1,p2 in zip(pp, sorted(pp)):
        if p1 != p2:
            c += 1

    if c == 2 or c == 0:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()
