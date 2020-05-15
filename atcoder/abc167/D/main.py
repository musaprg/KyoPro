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

N = None
K = None
A = None

def check(start):
    global N,K,A
    slow = A[start]
    fast = A[A[start]]
    while slow != fast:
        slow = A[slow]
        fast = A[A[fast]]

    slow = start
    while slow != fast:
        slow = A[slow]
        fast = A[fast]

    cycle_start = slow

    cycle_length = 1
    slow = A[slow]
    fast = A[A[fast]]
    while slow != fast:
        slow = A[slow]
        fast = A[A[fast]]
        cycle_length += 1

    return cycle_start, cycle_length

def main():
    global N,K,A
    N,K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [""] + A
    start,length = check(1)
    current = 1
    count = 0
    for _ in range(K):
        if current == start:
            break
        current = A[current]
        count += 1
    if current != start:
        return current
    K = (K-count)%length
    for _ in range(K):
        current = A[current] 
    return current

if __name__ == '__main__':
    print(main())
