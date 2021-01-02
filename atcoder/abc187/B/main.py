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
    points = []
    N = int(input())
    for _ in range(N):
        x,y = map(int, input().split())
        points.append((x,y))
    count = 0
    for i in range(N):
        for j in range(i+1,N):
            x1,y1 = points[i]
            x2,y2 = points[j]
            a = (y2-y1)/(x2-x1)
            count += int(-1 <= a <= 1)
    print(count)

if __name__ == '__main__':
    main()
