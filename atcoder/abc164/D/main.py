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

S = None

def main():
    global S
    S = input()
    if len(S) < 4:
        return 0
    count = 0

    for i in range(len(S)-3):
        for j in range(i+4,len(S)+1):
            #if check(i,j):
            #    print(i,j, S[i:j])
            #    count += 1
    return count

def check(i,j):
    cur = j-3
    a = int(S[i:cur])
    #n = a // 2
    n = (53*a)//107
    #print(a, n)
    if a != (2*n+n//53):
        return False
    print("hoge")
    return int(S[i:j])%2019==0
    #b = int(S[cur:cur+2])
    #cur += 2
    #c = int(S[cur])
    #return (c == (10-n)%10) and (b == (2*n-1+n//10)%100)

if __name__ == '__main__':
    print(main())
