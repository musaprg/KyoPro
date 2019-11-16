from math import sqrt

def solve(target):
    candidates = list(range(2,target))
    ans = 0

    for p in candidates:
        ans += p
        for i,n in enumerate(candidates):
            if n % p == 0:
                del candidates[i]

    return ans

if __name__ == '__main__':
    assert solve(10), 17
    print(solve(2000000))
