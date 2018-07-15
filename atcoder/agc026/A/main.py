N = int(input())
A = list(map(int, input().split()))

bef = 100000
count = 1
ans = 0

for a in A:
    # print("ans = %d" % ans)
    # print("now is %d" % a)
    if bef == a:
        count += 1
    else:
        ans += count // 2
        count = 1
        bef = a

ans += count // 2

print(ans)