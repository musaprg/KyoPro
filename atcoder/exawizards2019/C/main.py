from pprint import pprint

def main():
    N,Q = map(int, input().split())
    S = input()
    mcc = {}
    for s in S:
        mcc[s] = [0]*2
    for _ in range(Q):
        t,d = input().split()
        if d == "L":
            mcc[t][0] -= 1
        else:
            mcc[t][1] += 1
    pprint(mcc)

if __name__ == '__main__':
    main()
