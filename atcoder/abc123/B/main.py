import math
import sys

def main():
    a = []
    s = 0
    for _ in range(5):
        n = int(input())
        a.append(n)
        s += math.ceil(n/10)*10
    ans = sys.maxsize
    for n in a:
        ans = min(ans,s - math.ceil(n/10)*10 + n)
    print(ans)


if __name__ == '__main__':
    main()
