s1=input()
s2=input()
#if s2 in s1:
	#print('True')

def length(string):
    if not string:
        return 0
    else:
        return 1 + length(string[1:])
#print(length(s1))

def substring(s1):
	s=[]
	for i in range(length(s1)+1):
		for j in range(length(s1)+1):
			#print(s1[i:j])
			s.append(s1[i:j])
			#print(s)
	return s
l=substring(s1)
#print(l)
for i in l:
	if i == s2:
		print('True')


