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
sys.setrecursionlimit(10**6)

def check(n,a,b,c,t,l):
    tmp = 0
    if len(n) > l:
        return 0
    if n == "":
        return check(n+"3",a+1,b,c,t,l) + check(n+"5",a,b+1,c,t,l) + check(n+"7",a,b,c+1,t,l) + tmp
    if a and b and c and int(n) <= t:
        tmp = 1
    return check(n+"3",a+1,b,c,t,l) + check(n+"5",a,b+1,c,t,l) + check(n+"7",a,b,c+1,t,l) + tmp

def main():
    N = int(input())
    l = len(str(N))
    print(check("",0,0,0,N,l))

if __name__ == '__main__':
    main()
