def main():
    S=input()
    bf = S[0]
    for s in S[1::]:
        if bf == s:
            return False
        bf = s
    return True

if __name__ == '__main__':
    if main():
      print("Good")
    else:
      print("Bad")
