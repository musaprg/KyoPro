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
    A = sorted(A, reverse=True)
    ans = 0
    h = [-A.pop(0)]
    for a in A:
        t = heappop(h)
        ans += -t
        heappush(h,-a)
        heappush(h,-a)
    #ans += -heappop(h)
    print(ans)

if __name__ == '__main__':
    main()
