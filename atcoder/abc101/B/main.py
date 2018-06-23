N = int(input())
sn = 0
for s in str(N):
    sn += int(s)
if N % sn == 0:
    print("Yes")
else:
    print("No")