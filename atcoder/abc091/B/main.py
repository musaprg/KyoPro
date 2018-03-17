N = int(input())
ss = []
for i in range(N):
    ss.append(input())
M = int(input())
ts = []
for i in range(M):
    ts.append(input())
ans = 0
for s in ss:
    tmp = ss.count(s) - ts.count(s)
    if tmp > ans:
        ans = tmp
print(ans)

