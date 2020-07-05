import sys
from collections import defaultdict, Counter, deque
from itertools import accumulate, permutations, combinations
from operator import itemgetter
from bisect import bisect_left, bisect_right, bisect
from heapq import heappop, heappush
from fractions import gcd
from math import ceil, floor, sqrt, cos, sin, pi, log10
from copy import deepcopy
import numpy as np

# If you use recursive call, uncomment this code
#sys.setrecursionlimit(10**6)

def main():
    a,r,n = map(int, input().split())
    t = log10(a) + (n-1)*log10(r)
    if t > 9:
        return "large"
    else:
        return a * (r * (n-1))

if __name__ == '__main__':
    print(main())

