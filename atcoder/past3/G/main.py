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
    N,X,Y = map(int, input().split())
    X += 200
    Y += 200
    #maxgrid = max(X,Y)+1
    maxgrid = 400+1
    grids = [[False]*maxgrid for _ in range(maxgrid)] # (y,x)
    costs = [[sys.maxsize]*maxgrid for _ in range(maxgrid)]
    for _ in range(N):
        x,y = map(int, input().split())
        x += 200
        y += 200
        grids[y][x] = True
    queue = deque()
    start = maxgrid//2
    costs[start][start] = 0
    queue.appendleft((start,start))
    d = [(1,1),
        (0,1),
        (-1,1),
        (1,0),
        (-1,0),
        (0,-1)]
    while len(queue) != 0:
        cx,cy = queue.pop()
        for x,y in d:
            nx = cx + x
            ny = cy + y
            if not ((0 <= nx < maxgrid) and (0 <= ny < maxgrid)):
                continue
            if not grids[ny][nx]:
                tmp = costs[cy][cx] + 1
                if costs[ny][nx] > tmp:
                    costs[ny][nx] = tmp
                    queue.appendleft((nx,ny))

    print(costs[Y][X] if costs[Y][X] != sys.maxsize else -1)

if __name__ == '__main__':
    main()
