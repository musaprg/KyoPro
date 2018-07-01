from pprint import pprint
from statistics import median

N = int(input())
As = list(map(int, input().split(" ")))

As = [A - i for i, A in enumerate(As)]

# pprint(As)

b = int(median(As))

ans = 0

for A in As:
    ans += abs(A-b)

print(ans)