target = 600851475143

i = 2
ans = 0

while i <= target:
    #print("%d\t%d" % (i, target))
    if target % i == 0:
        target = target / i
        ans = i
    i += 1

print(ans)

