import math
import sys

def main():
    while True:
        d,e = map(int,input().split())
        ans = sys.maxsize
        if not d and not e:
            return
        for x in range(d+1):
            y = d-x
            ans = min(ans, abs(math.sqrt(float(x)**2+float(y)**2)-e))
        print(ans)

if __name__ == '__main__':
    main()
