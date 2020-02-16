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
    N,K = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    coord = bisect_left(A,0)
    A_left = A[:coord]
    A_right = A[coord:]
    num_left = len(A_left)
    num_right = len(A_right)
    kyoukaisen = num_left * num_right
    print("A:",A)
    print("coord:",coord)
    print(kyoukaisen)
    if K <= kyoukaisen:
        i = K // num_right
        j = (N-1) - (K % num_right)
        return A[i] * A[j]
    else:
        K -= kyoukaisen
        A_left = list(map(abs, reversed(A_left)))
        print("After K:",K)
        print("l comb:", num_left * (num_left-1)//2)
        print("r comb:", num_right * (num_right-1)//2)
        print("leftk:", K//num_left)
        print("rightk:", K//num_right)
        nidx_left = []
        nidx_right = []
        print("New A_left", list(A_left))
        print("New A_right", list(A_right))
        li,ri = 0,0
        for i in range(N):
            if li < num_left and ri < num_right:
                if A_left[li] < A_right[ri]:
                    nidx_right.append(i)
                    ri += 1
                else:
                    nidx_left.append(i)
                    li += 1
            elif li < num_left:
                nidx_left.append(i)
                li += 1
            else:
                nidx_right.append(i)
                ri += 1
        print(nidx_left)
        print(nidx_right)
        comb_left = combinations(nidx_left,2)
        comb_right = combinations(nidx_right,2)
        comb = list(comb_left) + list(comb_right)
        comb = sorted(comb)
        print(comb)
        print(comb[K-1])
        ans = 1
        try:
            ans *= A_left[nidx_left.index(comb[K-1][0])]
            ans *= A_left[nidx_left.index(comb[K-1][1])]
            print("hoge")
        except:
            pass
        try:
            ans *= A_right[nidx_right.index(comb[K-1][0])]
            ans *= A_right[nidx_right.index(comb[K-1][1])]
            print("fuga")
        except:
            pass
        return ans

if __name__ == '__main__':
    print(main())
