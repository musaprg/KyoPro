while True:
    n, r = list(map(lambda x: int(x), input().split(" ")))
    if n == 0 and r == 0:
        break
    cards = [i for i in range(1,n+1)]
    cards = cards[::-1]

    for i in range(r):
        p, c = list(map(lambda x: int(x), input().split(" ")))
        p -= 1
        cards = cards[p:p+c] + cards[0:p] + cards[p+c:]
    
    print(cards[0])