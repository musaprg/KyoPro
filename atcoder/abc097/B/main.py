from math import sqrt
x = int(input())
x2 = int(sqrt(x))
ans = 1
for i in range(x2):
  for k in range(x2-1):
    tmp = (i+1)**(k+2)
    if tmp<=x and ans<=tmp:
      ans = tmp
print(ans)