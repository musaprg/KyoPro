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
    A = map(int, input().split())
    for a in A: 
        if a % 2 == 0:
            if not (a % 3 == 0 or a % 5 == 0):
                return "DENIED"
    return "APPROVED"

if __name__ == '__main__':
    print(main())
