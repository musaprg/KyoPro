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
    n = int(input())
    aa = list(map(int,input().split()))
    bb = list(map(int,input().split()))
    cc = list(map(int,input().split()))
    ba = aa[0]-1
    ans = bb[ba]
    for a in aa[1::]:
        if ba+1 == a-1:
            ans += cc[ba]
        ba = a-1
        ans += bb[ba]
    print(ans)


if __name__ == '__main__':
    main()


