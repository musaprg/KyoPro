import sys

N = int(input())
S = input()
cw = [] # count W
cw.append(0)
for i, s in enumerate(S):
    i += 1
    if s == "W":
        cw.append(cw[i-1]+1)
    else:
        cw.append(cw[i-1])
#print(cw)

ans = 100000*3
for i in range(N):
    left = cw[i] # num of W
    right = (N-i-1)-(cw[N]-cw[i+1]) # num of E
    #print("left: %d, rw: %d, right: %d, %s, %s" % (left,cw[N]-cw[i+1],right,S[0:i],S[i+1:N]))
    tmp = left+right
    if ans>tmp:
        ans = tmp
print(ans)
