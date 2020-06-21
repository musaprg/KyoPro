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
    suma = sum(A)
    A = Counter(A)
    Q = int(input())
    for _ in range(Q):
        b,c = map(int, input().split())
        suma -= A[b]*b
        suma += A[b]*c
        A[c] += A[b]
        A[b] = 0
        print(suma)

if __name__ == '__main__':
    main()
