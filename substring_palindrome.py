string = input()
l=[]
def palindrome(a):
	if a == a[::-1]:
		return True
for i in range(len(string)+1):
	for j in range(len(string)+1):
		if palindrome(string[i:j]):
			l.append(string[i:j])
print(set(l))
