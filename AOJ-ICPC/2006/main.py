N = int(input())
d = []
d.append([])
d.append([".",",","!","?"])
d.append(["a","b","c"])
d.append(["d","e","f"])
d.append(["g","h","i"])
d.append(["j","k","l"])
d.append(["m","n","o"])
d.append(["p","q","r","s"])
d.append(["t","u","v"])
d.append(["w","x","y","z"])
for _ in range(N):
    nn = input()
    output = ""
    b = 0
    c = 0
    for n in nn:
        n = int(n)
        if n == 0 and b == 0:
            output += d[b][c%len(d[b])]
            c = 0
        c += 1
        b = n
    print(output)
