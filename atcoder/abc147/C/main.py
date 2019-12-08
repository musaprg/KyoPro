import sys
from collections import defaultdict, Counter, deque
from itertools import accumulate, permutations, combinations
from operator import itemgetter
from bisect import bisect_left, bisect_right, bisect
from heapq import heappop, heappush
from fractions import gcd
from math import ceil, floor, sqrt, cos, sin, pi
from copy import deepcopy
from pprint import pprint

# If you use recursive call, uncomment this code
sys.setrecursionlimit(10**6)

def main():
    global result,aa,N
    N = int(input())
    aa = []
    for _ in range(N):
        aaa = []
        na = int(input())
        for _ in range(na):
            x,y = map(int,input().split())
            aaa.append((x-1,y))
        aa.append(aaa)

    ans = 0
    for bm in range(1<<N):
        inconsisted = False
        #print("---")
        #print("{:08b}".format(bm))
        for i in range(N):
            #print("\t",i)
            if not bm & 1<<i:
                continue
            for x,y in aa[i]:
                if (bm & 1<<x) ^ y<<x:
                    inconsisted = True
                    break
            if inconsisted:
                break
        if inconsisted:
            continue
        tmp = 0
        for i in range(N):
            tmp += bm>>i & 0b1
        ans = max(ans,tmp)
    print(ans)
    

if __name__ == '__main__':
    main()
