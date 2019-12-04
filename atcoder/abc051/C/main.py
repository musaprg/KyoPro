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
    sx,sy,tx,ty = map(int, input().split())
    dx = ("R","L") if sx <= tx else ("L","R")
    dy = ("U","D") if sy <= ty else ("D","U")
    lx = abs(sx-tx)
    ly = abs(sy-ty)

    ans = ""
    for i in range(2):
        ans += dy[i]*ly
        ans += dx[i]*lx
   
    for i in range(2):
        inv = (i+1)%2
        ans += dx[inv]
        ans += dy[i]*(ly+1)
        ans += dx[i]*(lx+1)
        ans += dy[inv]

    print(ans)
    #print(len(ans))
    
if __name__ == '__main__':
    main()
