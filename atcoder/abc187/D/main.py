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
    towns = []
    N = int(input())
    numaoki = 0
    numtaka = 0
    for _ in range(N):
        a,b = map(int, input().split())
        numaoki += a
        towns.append((a,b,2*a+b))
    towns = sorted(towns, key=lambda x: x[2], reverse=True)
    # print(towns)
    c = 0
    # print("---")
    for t in towns:
        # print(numaoki, numtaka)
        if numaoki < numtaka:
            break
        a,b,_ = t
        numaoki -= a
        numtaka += a+b
        c += 1
    # print(numaoki)
    # print(towns)
    print(c)

if __name__ == '__main__':
    main()
