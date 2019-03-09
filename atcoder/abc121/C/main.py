def solve(m,ab):
    ans = 0
    for n in ab:
        if m == 0:
            break
        c = min(m,n[1])
        m -= c
        ans += c * n[0]
    return ans


def main():
    N,M = map(int, input().split())
    ab = []
    for _ in range(N):
        a,b = map(int, input().split())
        ab.append((a,b))
    ab.sort(key=lambda x: x[0])
    print(solve(M,ab))

if __name__ == '__main__':
    main()
