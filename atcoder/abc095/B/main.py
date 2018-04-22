n,x = map(int, input().split(" "))
ans = n
ms = []
for i in range(n):
    m = int(input())
    ms.append(m)
x = x - sum(ms)
ms.sort()
for m in ms:
    ans = ans + x // m
    x = x % m
print(ans)