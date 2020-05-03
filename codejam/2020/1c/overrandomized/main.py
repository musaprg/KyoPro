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

def solve():
    U = int(input())
    for _ in range(10**4):
        q,r = input().split()
        q = int(q)

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        print("Case #{0}: {1}".format(i+1, solve()))
