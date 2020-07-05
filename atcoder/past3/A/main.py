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
    s = input()
    t = input()
    if s == t:
        print("same")
    elif s.lower() == t.lower():
        print("case-insensitive")
    else:
        print("different")

if __name__ == '__main__':
    main()
