N = int(input())
ans = 0.0
for i in range(N):
    x,u = input().split()
    if u == "JPY":
        ans += int(x)
    else:
        ans += 380000.0 * float(x)
print("%.4f" % ans)
        
