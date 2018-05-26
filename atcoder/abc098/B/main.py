n = int(input())
s = input()
maxnum = 0
for i in range(1,n):
    num = 0
    s1 = set(s[0:i])
    s2 = set(s[i::])
    for c in s1:
        if c in s2:
            num += 1
    if maxnum < num:
        maxnum = num
print(maxnum)
