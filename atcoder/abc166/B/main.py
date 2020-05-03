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
    N,K = map(int, input().split())
    snukes = [0]*N
    for _ in range(K):
        d = int(input())
        A = list(map(int, input().split()))
        for a in A:
            snukes[a-1] += 1
    count = 0
    for snuke in snukes:
        if not snuke:
            count += 1
    print(count)

if __name__ == '__main__':
    main()
