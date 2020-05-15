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
    if len(s)+1 == len(t) and s == t[:len(t)-1]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
