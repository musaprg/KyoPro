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
    a,b,h,m = map(int, input().split())
    theta = (m/60 - (60*h+m)/(60*12)) * 2 * pi
    print(sqrt(a**2+b**2-2*a*b*cos(theta)))

if __name__ == '__main__':
    main()
