import sys
from collections import defaultdict, Counter, deque
from itertools import accumulate, permutations, combinations
from operator import itemgetter
from bisect import bisect_left, bisect_right, bisect
from heapq import heappop, heappush
from fractions import gcd
from math import ceil, floor, sqrt, cos, sin, pi
from copy import deepcopy
from pprint import pprint

# If you use recursive call, uncomment this code
#sys.setrecursionlimit(10**6)

def main():
    N = int(input())
    robots = []
    for _ in range(N):
        x,l = map(int, input().split())
        item = (x-l+1,x+l-1)
        robots.append(item)
    robots = sorted(robots, key=lambda x: x[1])
    pprint(robots)

    candidates = []
    
    for i in range(N-1):
        a = robots[i]
        b = robots[i+1]
        if a[1] >= b[0]:
            candidates.append((i,i+1))
    pprint(candidates)

    c = 0
    for i in range(len(candidates)-1):
        a = candidates[i]
        b = candidates[i+1]
        if a[1] == b[0]:
            c += 1
    ans = len(candidates)-c
    ans = N - ans

    print(ans)



if __name__ == '__main__':
    main()
