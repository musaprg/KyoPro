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


def solve(N,A,B):
    A = sorted(A)
    B = sorted(B)

    for a,b in zip(A,B):
        if a > b:
            return False

    # 例外

    return True


def main():
    N = int(input())
    A = list(map(int, input().split())) # 操作可能
    B = list(map(int, input().split()))

    if solve(N,A,B):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
