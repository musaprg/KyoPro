from pprint import pprint
N = int(input())
reds = []
for i in range(N):
    reds.append(tuple(map(int, input().split(" "))))
blues = []
for i in range(N):
    blues.append(tuple(map(int, input().split(" "))))
reds.sort(key=lambda x: (x[1], x[0]), reverse=True)
blues.sort()
picked = [False for _ in range(N)]
ans = 0
for blue in blues:
    for i, red in enumerate(reds):
        if blue[0] > red[0] and blue[1] > red[1] and not picked[i]:
            ans += 1
            picked[i] = True
            break
print(ans)