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
def check():
    ssum = 0
    for d in range(6):
        dd = 10**d
        count = 0
        for n in range(1*dd,dd*10):
            lunlunf = 1
            s = str(n)
            for i in range(len(s)-1):
                lunlunf *= (abs(int(s[i]) - int(s[i+1])) <= 1)
            if lunlunf:
                count += 1
        ssum += count
        print(dd,":",count, ssum)

def main():
    K = int(input())
    hoge = [9,35,110,327,956,2782]
    if K <= hoge[0]: # 10**0
        return getlunlun(0, K)
    for i in range(1,6):
        if K <= hoge[i]:
            return getlunlun(i, K-hoge[i-1])


if __name__ == '__main__':
    #print(main())
    check()
