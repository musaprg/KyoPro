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
    N,M = map(int, input().split())
    A = sorted(list(map(lambda x: int(x)-1, input().split())))
    if N == M:
        return 0
    if M == 0:
        return 1
    
    k = sys.maxsize
    for i in range(M-1):
        diff = A[i+1]-A[i]-1
        if diff:
            k = min(diff, k)
    firstdiff = A[0] - 0
    if firstdiff:
        k = min(k, firstdiff)
    lastdiff = N-A[-1]-1
    if lastdiff:
        k = min(k, lastdiff)

    count = 0

    if firstdiff:
        count += firstdiff//k
        count += int(firstdiff%k != 0)
    if lastdiff:
        count += lastdiff//k
        count += int(lastdiff%k != 0)

    for i in range(M-1):
        diff = A[i+1]-A[i]-1
        count += diff//k
        count += int(diff%k != 0)

    # print(A)
    # print(k)
    
    return count

if __name__ == '__main__':
    print(main())
