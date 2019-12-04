
def main():
    S = input()
    T = input()

    rs = S.replace("?","a")

    candidate = None

    for i in range(len(S)-len(T)+1):
        ts = S[i:i+len(T)]
        #print("checking:",ts)
        is_mismatched = False
        for ii in range(len(T)):
            if ts[ii] != "?" and ts[ii] != T[ii]:
                is_mismatched = True
                break
        if not is_mismatched:
            candidate = rs[:i] + T + rs[i+len(T):]
           
    return candidate if candidate else "UNRESTORABLE"

if __name__ == '__main__':
    print(main())
