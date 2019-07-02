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
    P = list(map(int, input().split()))
    count = 0
    for i in range(N-2):
        a = sorted(P[i:i+3])
        if a[1] == P[i+1]:
            count += 1 
    print(count)

if __name__ == '__main__':
    main()
