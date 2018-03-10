a = 1
b = 1
c = 0
max_limit = 4*(10**6)
ans = 0

while True:
    c = b + a
    if not c < max_limit:
        break
    if c % 2 == 0:
        ans += c
    a = b
    b = c

print(ans)
