import sys
N = int(input())
for i in range(0,30):
    for j in range(0,30):
        tmp = 4*i+7*j
        if tmp <= 100:
            if tmp == N:
                print("Yes")
                sys.exit(0)
        else:
            break
print("No")

