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

def solve(N,D):
    if D[0]:
        return 0

    try:
        _ = D[1::].index(0)
        return 0
    except:
        pass
    
    nums = Counter(D)
    nums = sorted(nums.items())
    if len(nums) != nums[-1][0]+1:
        return 0
        
    #print(nums)
    ans = 1
    for i in range(len(nums)-1):
        ans *= nums[i][1]**nums[i+1][1]
        ans %= 998244353
    return ans

def main():
    N = int(input())
    D = list(map(int, input().split()))
    
    print(solve(N,D))

if __name__ == '__main__':
    main()
