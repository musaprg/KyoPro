N, M = map(int, input().split())
Ain = list(map(int, input().split()))
A = []
A.append(Ain[0])
for i, a in enumerate(Ain[1::]):
    A.append(a + A[i])
A.append(0) # A[-1]
    
ans = 0
for l in range(N):
    for r in range(l,N):
        if (A[r]-A[l-1]) % M == 0:
            ans += 1
print(ans)



