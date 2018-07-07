S = input()
w = int(input())
print("".join([s for i,s in enumerate(S) if i % w == 0]))