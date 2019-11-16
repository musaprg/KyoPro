import sys
from collections import defaultdict, Counter, deque
from itertools import accumulate, permutations, combinations
from operator import itemgetter
from bisect import bisect_left, bisect_right, bisect
from heapq import heappop, heappush
from fractions import gcd
from math import ceil, floor, sqrt, cos, sin, pi, factorial
from copy import deepcopy

# If you use recursive call, uncomment this code
#sys.setrecursionlimit(10**6)

def main():
    N = int(input())
    xxyy = [tuple(map(int, input().split())) for _ in range(N)]
    ssum = 0
    for a,b in combinations(xxyy,2):
        #print(a,b) 
        dx = (a[0] - b[0])**2
        dy = (a[1] - b[1])**2
        tmp = sqrt(dx+dy)
        #print(tmp)
        ssum += tmp
    #print("---")
    #print(ssum)
    print(ssum*2/N)

if __name__ == '__main__':
    main()
