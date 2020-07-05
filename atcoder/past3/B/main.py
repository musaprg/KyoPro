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
    N,M,Q = map(int, input().split())
    points = [N]*M
    solved = [[] for _ in range(N)]
    for _ in range(Q):
        s = list(map(int, input().split()))
        if s[0] == 1:
            n = s[1]-1
            print(sum([points[x] for x in solved[n]]))
        else:
            n = s[1]-1
            m = s[2]-1
            solved[n].append(m)
            points[m] -= 1

if __name__ == '__main__':
    main()
