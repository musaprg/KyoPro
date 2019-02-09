
def main():
    paths = [0]*4
    for i in range(3):
        a,b = map(int, input().split())
        paths[a-1] += 1
        paths[b-1] += 1
    paths.sort()
    if paths == [1,1,2,2] or paths == [0,0,0,3]:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    print(main())

