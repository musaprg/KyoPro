import sys
from collections import defaultdict, Counter, deque
from itertools import accumulate, permutations, combinations
from operator import itemgetter
from bisect import bisect_left, bisect_right, bisect
from heapq import heappop, heappush
from fractions import gcd
from math import ceil, floor, sqrt, cos, sin, pi
import math
from copy import deepcopy

# If you use recursive call, uncomment this code
sys.setrecursionlimit(10**6)

def comb(n,r):
    if n < r:
        return 0
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def main():
    n,k = map(int, input().split())
    redn = n-k
    modn = 10**9+7
    for i in range(1,k+1):
        ans = comb(redn+1,i)*comb(k-1,i-1)%modn
        print(ans)
        

if __name__ == '__main__':
    main()
