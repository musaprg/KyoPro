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
    B = list(map(int, input().split()))

    ans = 0

    k = min(A[0], B[0])
    ans += k
    A[0] -= k
    B[0] -= k

    for i in range(1,N):
        k = min(A[i], B[i-1])
        ans += k
        A[i] -= k
        B[i-1] -= k

        k = min(A[i], B[i])
        ans += k
        A[i] -= k
        B[i] -= k

    k = min(A[-1], B[-1])
    ans += k

    print(ans)


if __name__ == '__main__':
    main()
