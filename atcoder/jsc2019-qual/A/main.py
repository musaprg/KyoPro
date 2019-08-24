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
    M,D = map(int, input().split())
    days = set()
    for d in range(D+1):
        d_1 = d % 10
        d_10 = d // 10
        if d_1 < 2 or d_10 < 2:
            continue
        m = d_1*d_10
        day = (m,d)
        if (day not in days) and (m <= M):
            days.add(day)
    print(len(days))

if __name__ == '__main__':
    main()
