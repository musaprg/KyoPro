def check(s,t):
	for i in range(0,len(s)):
		tmp = s[len(s)-i::] + s[0:len(s)-i]
		if tmp == t:
			return "Yes"
	return "No"

if __name__ == '__main__':
	s, t = input(), input()
	print(check(s,t))
