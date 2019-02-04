import math
 
def solve(N,M,Xs):
    if N >= M:
        return 0
 
    Ds = [abs(Xs[i]-Xs[i+1]) for i in range(len(Xs)-1)] # Ds[j] := distance between j and j+1
 
    Ds.sort()
    #print(Ds)
    #print(math.ceil(N/2))

    #ntake = math.ceil(N/2)
    ntake = N-1
 
    return sum(Ds[0:len(Ds)-ntake])
 
def main():
    N, M = map(int, input().split())
    Xs = list(map(int, input().split()))
    Xs.sort()
    print(solve(N,M,Xs))
 
 
if __name__ == '__main__':
    main()
