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
    counts = [[] for _ in range(N)]
    for i in range(N):
        S = set(input())
        for s in S:
            counts[i].append(s)
            counts[i] = sorted(counts[i])
    mid = N//2
    ans = ""
    midstr = ""
    for i in range(mid):
        is_found = False
        for s in counts[i]:
            revidx = N-i-1
            idx = bisect_left(counts[revidx], s)
            if idx != len(counts[revidx]) and counts[revidx][idx] == s:
                ans += s
                is_found = True
                break
        if not is_found:
            return -1
    if N % 2 == 0:
        return ans + ans[::-1]
    else:
        return ans + counts[mid][0] + ans[::-1]

if __name__ == '__main__':
    print(main())
