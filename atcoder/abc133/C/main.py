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
    L,R = map(int, input().split())

    ans = sys.maxsize

    # 0 がある場合
    # 0 がない場合→全探索

    if R//2019 - (L-1)//2019 > 0:
        return 0
    
    if R//673 - (L-1)//673 > 0 and R//3 - (L-1)//673 > 0:
        return 0

    for i in range(L,R+1):
        for j in range(i+1,R+1):
            ans = min(ans, i*j%2019)
    
    return ans

if __name__ == '__main__':
    print(main())
