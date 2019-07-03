from collections import defaultdict
import sys
import copy

def main():
    while True:
        t = int(input())
        if not t:
            return
        cclist = (10,50,100,500)
        cc = list(map(int,input().split())) # 10 50 100 500
        cmin = sys.maxsize
        cand = None
        for i in range(cc[3]+1): # 500
            for j in range(cc[2]+1): # 100
                for k in range(cc[1]+1): # 50
                    for l in range(cc[0]+1): # 10
                        result = 500*i+100*j+50*k+10*l
                        if result < t:
                            continue
                        tmp = otsuri(result-t) # [500, 100, 50, 10]
                        # if (i and tmp[0]) or (j and tmp[1]) or (k and tmp[2]) or (l and tmp[3]):
                        #     continue
                        if tmp < cmin:
                            cmin = tmp
                            cand = (l,k,j,i)
        for c,n in zip(cclist, cand):
            if n == 0:
                continue
            print(c,n)

                        

def otsuri(n: int):
    res = 0
    for i,c in enumerate([500,100,50,10]):
        res += n // c
        n %= c
    return res


if __name__ == '__main__':
    main()