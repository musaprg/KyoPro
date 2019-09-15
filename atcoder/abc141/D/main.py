import sys
from collections import defaultdict, Counter, deque
from itertools import accumulate, permutations, combinations
from operator import itemgetter
from bisect import bisect_left, bisect_right, bisect
from heapq import heappop, heappush
from fractions import gcd
from math import ceil, floor, sqrt, cos, sin, pi, log2
from copy import deepcopy

# If you use recursive call, uncomment this code
#sys.setrecursionlimit(10**6)

def main():
    N,M = map(int, input().split())
    A = []
    list(map(lambda x: heappush(A, -1*int(x)), input().split()))
    for _ in range(M):
        a = -1*heappop(A)
        heappush(A, a//2 * -1)
    ans = 0
    for _ in range(N):
        ans += -1 * heappop(A)
    print(ans)

if __name__ == '__main__':
    main()
