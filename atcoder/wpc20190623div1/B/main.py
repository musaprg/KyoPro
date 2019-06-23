import copy

def main():
    while True:
        # print("===============================================================================")
        n,m,t,p = map(int,input().split())
        if not n and not m and not t and not p:
            return

        dlist,clist = [],[]
        
        for _ in range(t):
            d,c = map(int,input().split())
            dlist.append(d)
            clist.append(c)

        coorlist = [tuple(map(int,input().split())) for _ in range(p)]

        oldm = [[1 for _ in range(m)] for _ in range(n)]

        for d,c in zip(dlist,clist):
            if d == 1:
                newm = [[0]*m for _ in range(max(n-c,c))]
                for i in range(n):
                    for j in range(c):
                        newm[i][j] = 
            else:
                newm = [[0 for _ in range(m)] for _ in range(max(n-c,c))]
                for i in range(n):
                    for j in range()

        visualize(oldm)

        ans = 0
        for c in coorlist:
            print(oldm[c[0]][c[1]])


def visualize(mmap):
    print("------------------")
    for j in range(len(mmap[0])):
        print('|', end="")
        for i in range(len(mmap)):
            print(mmap[i][len(mmap[0])-1-j], '|', end="")
        print()
    print("------------------")


if __name__ == '__main__':
    main()
