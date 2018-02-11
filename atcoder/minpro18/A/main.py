s = input()
s1 = s[0:3]
s2 = s[3:]
if s1 == "yah":
    if len(s2) == 2 and s2[0] == s2[1]:
        print("YES")
    else:
        print("NO")
else:
    print("NO")