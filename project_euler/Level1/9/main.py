from math import sqrt

def solve(target):
    for a in range(1,target):
        for b in range(a+1,target):
            for c in range(b+1, target):
                if a+b+c == target and a**2+b**2 == c**2:
                    return a*b*c

if __name__ == '__main__':
    print(solve(1000))
