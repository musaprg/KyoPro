N, T = map(int, input().split())
ans = 5000
for i in range(N):
  c, t = map(int, input().split())
  if t <= T and c <= ans:
      ans = c
if ans == 5000:
    print("TLE")
else:
    print(ans)