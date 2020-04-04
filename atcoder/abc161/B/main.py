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
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    threshold = sum(A)/(4*M)
    count = 0
    for a in A:
        if a >= threshold:
            count += 1
        if count == M:
            return "Yes"
    return "No"

if __name__ == '__main__':
    print(main())
