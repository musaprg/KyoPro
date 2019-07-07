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


def d(yy,zz):
    ans = 0
    for i in range(len(yy)):
        ans += (yy[i]-zz[i])**2
    return sqrt(ans)

def main():
    N,D = map(int, input().split())
    xx = []
    for _ in range(N):
        xx.append(list(map(int,input().split())))
    
    c = 0
    for i in range(N):
        for j in range(i+1,N):
            if d(xx[i], xx[j]).is_integer():
                c += 1
    
    print(c)

if __name__ == '__main__':
    main()
