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
    n,k = map(int, input().split())
    q = (k-1) % (n-1)
    a = n*k-1-q
    return a // (n-1)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        print(main())
