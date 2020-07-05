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

nodes = None
edges = None

def main():
    N,M,Q = map(int, input().split())
    edges = [[False]*N for _ in range(N)]
    for _ in range(M):
        u,v = map(int, input().split())
        u -= 1
        v -= 1
        edges[u][v] = edges[v][u] = True
    nodes = list(map(int, input().split()))
    for _ in range(Q):
        s = list(map(int, input().split()))
        x = s[1]-1
        print(nodes[x])
        if s[0] == 1:
            for i in range(N):
                if edges[x][i]:
                    nodes[i] = nodes[x]
        else:
            nodes[x] = s[2]

if __name__ == '__main__':
    main()
