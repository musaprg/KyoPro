def solve(target):
    primenums = []

    n = 1

    while len(primenums) < target:
        n += 1
        is_prime = True
        for i in primenums:
            if n % i == 0:
                is_prime = False
                break
        if not is_prime:
            continue
        primenums.append(n)

    return primenums.pop()

if __name__ == '__main__':
    print(solve(10001))
    #print(solve(6))
