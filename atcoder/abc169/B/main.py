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
    A = list(map(int, input().split()))
    ans = 1
    threshold = 10**18
    if 0 in A:
        return 0
    for a in A:
        ans *= a
        if ans > threshold:
            return -1
    return ans

if __name__ == '__main__':
    print(main())
