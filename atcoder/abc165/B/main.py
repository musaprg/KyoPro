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
    X = int(input())
    ans = 100
    i = 0
    while True:
        if ans >= X:
            break
        ans += int(ans * 0.01)
        i += 1
    print(i)

if __name__ == '__main__':
    main()
