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
    check = defaultdict(int)
    N = int(input())
    ss = set()
    for _ in range(N):
        s = input()
        ss.add(s)
    for s in ss:
        tmp = s
        if s[0] == "!":
            tmp = tmp[1::]
        check[tmp] += 1
    for k,v in check.items():
        if v == 2:
            return k
    return "satisfiable"

if __name__ == '__main__':
    print(main())
