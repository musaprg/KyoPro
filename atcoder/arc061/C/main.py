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

def parse():

    return 

def main():
    S = input()
    ans = 0
    nn = len(S)-1
    for i in range(1<<nn): # bit flag to insert '+'
        #print(bin(i))
        end = len(S)
        for j in range(nn):
            if 1<<j & i:
                start = len(S)-1-j
                s = S[start:end]
                #print(start,end)
                #print(s)
                try:
                    ans += int(s)
                except:
                    pass
                end = start
        s = S[:end]
        #print(s)
        try:
            ans += int(s)
        except:
            pass
        #print()
    print(ans)



if __name__ == '__main__':
    main()
