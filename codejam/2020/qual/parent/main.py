import sys
from collections import defaultdict, Counter, deque
from itertools import accumulate, permutations, combinations
from operator import itemgetter
from bisect import bisect_left, bisect_right, bisect
from heapq import heappop, heappush
from fractions import gcd
from math import ceil, floor, sqrt, cos, sin, pi
from copy import deepcopy

from enum import Enum

# If you use recursive call, uncomment this code
#sys.setrecursionlimit(10**6)

def solve():
    N = int(input())
    tasks = []
    for i in range(N):
        start,end = map(int,input().split())
        tasks.append((i,(start,end)))
    shifts = [""] * N
    tasks = sorted(tasks, key=lambda x: x[1][1], reverse=True)
    c_task_s = sys.maxsize
    j_task_s = sys.maxsize
    for task in tasks:
        start, end = task[1]
        if c_task_s >= end:
            c_task_s = start
            shifts[task[0]] = "C"
        elif j_task_s >= end:
            j_task_s = start
            shifts[task[0]] = "J"
        else:
            return "IMPOSSIBLE"
    return "".join(shifts)


def main():
    T = int(input())
    for i in range(1,T+1):
        print("Case #%d: %s" % (i, solve()))

if __name__ == '__main__':
    main()
