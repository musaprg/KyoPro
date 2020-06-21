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
    aa = list(map(int,input().split()))
    S = aa[0]
    for a in aa[1::]:
        S ^= a
    ans = []
    for a in aa:
        ans.append(str(S ^ a))
    print(" ".join(ans))

if __name__ == '__main__':
    main()
