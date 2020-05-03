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
    N,M = map(int, input().split())
    H = list(map(int, input().split()))
    nodes = [[] for _ in range(N)]
    for _ in range(M):
        a,b = map(int,input().split())
        nodes[a-1].append(b-1) 
        nodes[b-1].append(a-1)
    count = 0
    for i in range(N):
        res = True
        if len(nodes[i]) == 0:
            count += 1
            continue
        for n in nodes[i]:
            res = res and (H[n] < H[i])
        count += int(res)
    print(count)
if __name__ == '__main__':
    main()
