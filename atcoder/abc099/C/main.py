import math

N = int(input())

def calc(n, i):
    if n == 0:
        return i
    elif n < 6:
        return i + n
    elif n < 9:
        return i + (n - 6 + 1)
    else:
        return min(
            calc(n - 9**int(math.log(n,9)), i+1),
            calc(n - 6**int(math.log(n,6)), i+1)
        )
    
print(calc(N, 0))