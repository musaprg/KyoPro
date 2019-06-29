import math

def main():
    while True:
        r0,w0,c,r = map(int,input().split())
        if not r0 and not w0 and not c and not r:
            return
        current = r0/w0
        ans = 0
        if c < current:
            ans = 0
        else:
            ans = math.ceil((c*w0-r0)/r)
        
        print(ans)
            

if __name__ == '__main__':
    main()
