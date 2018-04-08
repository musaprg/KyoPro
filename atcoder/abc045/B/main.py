
def main(sa, sb, sc):
    cs = "a"
    while True:
        if cs == "a":
            if len(sa) == 0:
                return "A"
            cs = sa.pop()
        elif cs == "b":
            if len(sb) == 0:
                return "B"
            cs = sb.pop()
        else:
            if len(sc) == 0:
                return "C"
            cs = sc.pop()

if __name__ == '__main__':
    sa = list(input())
    sb = list(input())
    sc = list(input())
    print(main(sa,sb,sc))
