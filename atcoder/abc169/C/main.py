import sys
from collections import defaultdict, Counter, deque
from itertools import accumulate, permutations, combinations
from operator import itemgetter
from bisect import bisect_left, bisect_right, bisect
from heapq import heappop, heappush
from fractions import gcd
from math import ceil, floor, sqrt, cos, sin, pi
from copy import deepcopy
from decimal import *

# If you use recursive call, uncomment this code
#sys.setrecursionlimit(10**6)

def main():
    N,M = input().split()
    getcontext().prec = 20
    getcontext().rounding = ROUND_DOWN
    N = Decimal(N)
    M = Decimal(M)
    res = N*M
    print(res.quantize(Decimal('1.'), rounding=ROUND_DOWN))


if __name__ == '__main__':
    main()
