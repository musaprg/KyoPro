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
    A = list(map(int, input().split())) # 0 ~ N-1 0-indexed
    truesum = sum(A)

    for m_fixed in range(max(A[-1],A[0])): # 0を固定
        if m_fixed%2!=0:
            continue
        if A[-1]-m_fixed//2 < 0 or A[0]-m_fixed//2 < 0:
            continue
        f = False
        mm = [0]*N
        mm[0] = m_fixed
        aa = deepcopy(A)
        aa[-1] -= m_fixed//2
        aa[0] -= m_fixed//2
        if aa[-1] < 0 or aa[0] < 0:
            continue
        for i in range(1,N):
            mm[i] = aa[i-1]*2
            if aa[i] < aa[i-1]:
                f = True
                break
            aa[i] -= aa[i-1]
            aa[i-1] = 0
        if f or truesum != sum(mm):
            continue
        return mm
        


if __name__ == '__main__':
    print(*main(), sep=" ")
