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
    N,M,T = map(int, input().split())
    c = 0
    rem = N
    for _ in range(M):
        a,b = map(int,input().split())
        down = floor(a - c - 0.5) + 1
        rem -= down
        if rem <= 0:
            return False
        up = floor(b - a - 0.5) + 1
        rem += up
        rem = min(rem, N)
        if rem <= 0:
            return False
        c = b
    rem -= floor(T - c - 0.5) + 1
    return rem > 0

if __name__ == '__main__':
    print("Yes" if main() else "No")
