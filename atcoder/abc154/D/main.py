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

def get_range_sum(l,s,e):
    return l[e] - l[s]

def main():
    N,K = map(int, input().split())
    pp = list(map(int, input().split()))
    pp_rui = defaultdict(int)
    for i in range(N):
        pp_rui[i+1] = pp_rui[i] + pp[i]
    #print(pp_rui)
    emax = 0
    cc = K/2
    for i in range(N-K+1):
        res = get_range_sum(pp_rui, i, i+K) + K
        res = res / 2
        #print(i, res)
        emax = max(emax, res)
    print("{:.12f}".format(emax))

if __name__ == '__main__':
    main()
