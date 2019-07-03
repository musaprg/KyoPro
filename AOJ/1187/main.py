import sys

def main():
    while True:
        M,T,P,R = map(int,input().split())
        if not M and not T and not P and not R:
            return
        prob = [[0]*(P+1) for _ in range(T+1)]
        result = dict([(t,[0,sys.maxsize]) for t in range(1,T+1)]) # (t,m,p)
        for _ in range(R):
            m,t,p,j = map(int,input().split())
            if j == 0:
                result[t][0] += prob[t][p] + m
                result[t][1] += 1
            else:
                prob[t][p] += 20
        result = list(result.items())
        result = sorted(result, key=lambda x: (-1*x[1][1], x[1][0], -1*x[0]))

        print(result[0][0], end="")
        for i in range(1,T):
            if result[i][1][0] == result[i-1][1][0] and result[i][1][1] == result[i-1][1][1]:
                print("={}".format(result[i][0]), end="")
            else:
                print(",{}".format(result[i][0]), end="")
        print()

if __name__ == '__main__':
    main()