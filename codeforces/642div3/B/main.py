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
    n,k = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    if a[0] > b[-1]:
        return sum(a)
    ans = 0
    for i in range(n):
        if i < k and a[i] < b[n-1-i]:
            ans += b[n-1-i]
        else:
            ans += a[i]
    return ans
        

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        print(main())
