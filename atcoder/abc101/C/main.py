import math

N,K = map(int, input().split(" "))
A = list(map(int, input().split(" ")))
llen = A.index(1) # num of element (left)
rlen = N-llen-1
# assert N == llen+rlen+1
# tmp = (K-1)*(llen//K)
# remain = 0
# if tmp == 0:
#     remain = llen + rlen
# else:
#     remain = llen-tmp + rlen
# print(tmp)
# print(remain)
if llen % (K-1) == 0:
    print(llen//(K-1) + math.ceil(rlen/(K-1)))
elif rlen % (K-1) == 0:
    print(rlen//(K-1) + math.ceil(llen/(K-1)))
else:
    tmp = math.ceil(llen/(K-1))
    rlen -= (K-1)*tmp - llen
    print(tmp + rlen//(K-1))